from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import requests
<<<<<<< Updated upstream
=======
import os
from waitress import serve

>>>>>>> Stashed changes

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5000", "http://localhost:5000", "https://chat.openai.com"])


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
<<<<<<< Updated upstream
        for i, place in enumerate(possibleNearbyPlaces):
            reviews = get_reviews(place.place_id, api_key)
            all_reviews.push(reviews)
=======
        for place in possibleNearbyPlaces:
            reviews = get_reviews(place["place_id"])
            all_reviews.append(reviews)
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
if __name__ == '__main__':
    app.run(debug=False)
=======
@app.route("/places", methods=["GET"])
def get_place_reviews():
    location = request.args.get("location")
    radius = request.args.get("radius")
    type_of = request.args.get("type")

    try:
        # Convert radius to integer
        radius = int(radius)
        reviews = proccessPlaces(location, radius, type_of)
        # Return a JSON response
        return jsonify({"reviews": reviews})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/.well-known/ai-plugin.json")
def serve_ai_plugin():
    return send_from_directory(".", "ai-plugin.json", mimetype="application/json")


@app.route("/.well-known/openapi.yaml")
def serve_openapi_yaml():
    return send_from_directory(".", "openapi.yaml", mimetype="text/yaml")


if __name__ == "__main__":
    serve(app, host="127.0.0.1", port=5000)
>>>>>>> Stashed changes
