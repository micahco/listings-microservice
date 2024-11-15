# listings-microservice

## How to Run the Microservice

I have provided a devcontainer which provides a Docker environment containing all the tools necessary to run the program. Please refer to [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers) for more information about container development.

If you already have Python installed on your computer, you can also install the necessary requirements in a [virtual environemnet](https://docs.python.org/3/tutorial/venv.html).

Once you have the environment ready, you can run the server with: `make dev` or `python main.py`.

## How to Request Data

This microservice is an HTTP API. To request listings data, make a [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) request to the root directoy.

### Description
`GET /<zip_code>`: Retrieve a list of property listings in a specified zip code with optional filters for price, square footage, number of bedrooms, and bathrooms.

### Path Parameters
| Parameter  | Required | Description                                      |
|------------|----------|--------------------------------------------------|
| `zip_code` | Yes      | A 5-digit postal code. Must be numeric and exactly 5 digits long. |


### Query Parameters
| Parameter   | Required | Default | Description                         |
|-------------|----------|---------|-------------------------------------|
| `limit`     | No       | 10      | The maximum number of listings to return. |
| `max_price` | No       | None    | The maximum price of the listings.  |
| `max_sqft`  | No       | None    | The maximum square footage of the listings. |
| `max_beds`  | No       | None    | The maximum number of bedrooms.     |
| `max_baths` | No       | None    | The maximum number of bathrooms.    |

### Request Example
```http
GET /97370?limit=5&max_price=400000&max_sqft=2500&max_beds=3&max_baths=2
```

If you have the server running locally on the default port:

[http://127.0.0.1:5000/97370?limit=3&max_price=400000&max_sqft=2500](http://127.0.0.1:5000/97370?limit=3&max_price=400000&max_sqft=2500)

## How to Receive Data

Python example using the [requests](https://pypi.org/project/requests/) library:

```
import requests


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

```

### UML

![UML](https://kroki.io/mermaid/svg/eNqFkMFKA0EQRO_5ij4q6OYusiIqkoMaNHiVYbeiDZPtsWYSiV9vu4uJkgX7MjTUq6rpjPc1ugbXGl4ZVhPxuYqKrpzW9Z02tAxutMGZ3N4sZHr-qemlsRb1RVVVvfy36gB6DlHbUCA_3P_IPDBDvBa3koKXQgHzGPeIEIvxcj5z6uFpIfz-TS7yoeXN2W200PbgXnkQR5Q1u-xvTtZ58lGiJbAoshgFpPF4LH6405hDVC9hS9k7DQb35pewDSh_O8yWQ8zJzqtfd46TL8Bvk6E)
