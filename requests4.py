# Handle errors

import requests

try:
    response = requests.get(
        "https://api.example.com/data",
        timeout=10
    )

    response.raise_for_status()

    print(response.json())

except requests.exceptions.RequestException as e:
    print("Request failed:", e)