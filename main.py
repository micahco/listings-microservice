import os
from dotenv import load_dotenv
import requests
from flask import Flask, request, jsonify

load_dotenv()

url = "https://realtor-com4.p.rapidapi.com/properties/list"

headers = {
    "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
    "x-rapidapi-host": "realtor-com4.p.rapidapi.com",
    "Content-Type": "application/json"
}

app = Flask(__name__)


@app.route('/<string:zip_code>', methods=['GET'])
def listings(zip_code):
    # Validate parameter
    if not zip_code.isdigit() or len(zip_code) != 5:
        return jsonify({"error": "Invalid zip code format"}), 400

    # Parse query arguments
    limit = request.args.get('limit', type=int)
    max_price = request.args.get('max_price', type=int)
    max_sqft = request.args.get('max_sqft', type=int)
    max_beds = request.args.get('max_beds', type=int)
    max_baths = request.args.get('max_baths', type=int)

    payload = {
        "query": {
            "postal_code": zip_code,
        },
        "limit": 10,  # Default value
        "sort": {
            "direction": "desc",
            "field": "list_date"
        }
    }

    if limit is not None:
        payload["limit"] = limit

    if max_price is not None:
        payload["query"]["list_price"] = {"max": max_price}

    if max_sqft is not None:
        payload["query"]["sqft"] = {"max": max_sqft}

    if max_beds is not None:
        payload["query"]["beds"] = {"max": max_beds}

    if max_baths is not None:
        payload["query"]["baths"] = {"max": max_baths}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        try:
            properties = response.json()["data"]["home_search"]["properties"]
            return jsonify(properties)
        except KeyError:
            return jsonify({"error": "No property data found"}), 404

    except requests.exceptions.HTTPError as http_err:
        return jsonify({"error": f"HTTP error occurred: {http_err}"}), response.status_code
    except requests.exceptions.RequestException as req_err:
        return jsonify({"error": f"Request error occurred: {req_err}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
