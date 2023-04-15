from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

api_key = 'example_key
'
@app.route('/get_place_details', methods=['GET'])
def proccessPlaces():
    # Get the place_id and api_key from query parameters
    place_id = request.args.get('preferences')
    radius = request.args.get('radius')

    response = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/output?parameters")

    if response.status_code == 200:

    #iterate through all places and iterate through all its reviews to find best
        possibleNearbyPlaces = response.results
        all_reviews = []
        for i, place in enumerate(possibleNearbyPlaces):
            reviews = get_reviews(place.place_id, api_key)
            all_reviews.push(reviews)
        return all_reviews
    else:
        return jsonify({"error": f"Error: {response.status_code}"}), response.status_code

@app.route('/get_reviews', methods=['GET'])
def get_reviews(place_id, api_key):
    response = requests.get("https://maps.googleapis.com/maps/api/place/details/json?placeid={place_id}&key={api_key}")
    if response.status_code == 200:
        reviewArray = response.reviews # Parse the JSON response
        return jsonify(reviewArray)
    else:
        return jsonify({"error": f"Error: {response.status_code}"}), response.status_code

if __name__ == '__main__':
    app.run(debug=False)