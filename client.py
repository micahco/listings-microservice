import requests

# TEST PROGRAM
#
# This is an example client request

zip_code = "97370"
try:
    response = requests.get(f"http://127.0.0.1:5000/{zip_code}", params={
        "limit": 3,
        "max_price": 400000,
        "max_sqft": 2500,
        "max_beds": 3,
        "max_baths": 2,
    })
    response.raise_for_status()
    listings = response.json()
    for i, listing in enumerate(listings):
        price = listing["list_price"]
        sqft = listing["description"]["sqft"]
        beds = listing["description"]["beds"]
        baths = listing["description"]["baths_consolidated"]
        print(f"\nLISTING {i+1}")
        print(f"Price: {price}")
        print(f"SQFT: {sqft}")
        print(f"Beds: {beds}")
        print(f"Baths: {baths}")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")

except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
