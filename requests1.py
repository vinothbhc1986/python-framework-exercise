import requests
# to make HTTP/API requests
response = requests.get("https://api.github.com")

print(response.status_code)
print(response.text)

# get json data
print(response.json())