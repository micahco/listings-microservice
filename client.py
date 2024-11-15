import requests

# This is an example client request


def fetch_listings(zip_code, queries=None):
    if queries is None:
        queries = {}

    url = f"http://127.0.0.1:5000/{zip_code}"

    try:
        response = requests.get(url, params=queries)
        response.raise_for_status()
        data = response.json()
        print(data)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")


fetch_listings("97370", {
    "limit": 5,
    "max_price": 400000,
    "max_sqft": 2500,
    "max_beds": 3,
    "max_baths": 2,
})
