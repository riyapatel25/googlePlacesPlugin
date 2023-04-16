from flask import Flask, jsonify, request
import requests
import os


app = Flask(__name__)

api_key = os.environ.get("GOOGLE_API_KEY")


def get_reviews(place_id):
    params = {
        "place_id": place_id,
    }
    url = (
        f"https://maps.googleapis.com/maps/api/place/details/json"
        f"?place_id={params['place_id']}"
        f"&key={api_key}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        reviewArray = (
            response.json().get("result", {}).get("reviews", [])
        )  # Parse the JSON response
        return reviewArray
    else:
        return []


@app.route("/get_place_details/<location>/<int:radius>/<type_of>", methods=["GET"])
def proccessPlaces(location, radius, type_of):
    params = {"key": api_key, "location": location, "radius": radius, "type": type_of}
    url = (
        f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        f"?location={params['location']}"
        f"&radius={params['radius']}"
        f"&type={params['type']}"
        f"&key={api_key}"
    )
    response = requests.get(url)

    if response.status_code == 200:
        possibleNearbyPlaces = response.json().get("results", [])
        all_reviews = []
        for place in possibleNearbyPlaces:
            reviews = get_reviews(place['place_id'])
            all_reviews.append(reviews)
        return all_reviews
    else:
        return []


if __name__ == "__main__":
    app.run(debug=False)
