# Send query parameters

import requests

params = {
    "q": "python",
    "page": 1
}

response = requests.get(
    "https://api.github.com",
    params=params
)

print(response.url)
print(response.json())
