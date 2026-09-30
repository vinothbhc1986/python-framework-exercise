# POST request

import requests

data = {
    "username": "john",
    "email": "john@example.com"
}

response = requests.post(
    "https://api.github.com",
    json=data
)

print(response.status_code)
print(response.json())