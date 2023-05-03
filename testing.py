import requests
import json

consumet_api_endpoint = "https://api.consumet.org/anime/gogoanime"

title = "Demon Slayer"
response = requests.get(url=f"{consumet_api_endpoint}/{title}")

# if request is successful...
if response.status_code >= 200 and response.status_code < 300:
    data = response.json()["results"]
    print(json.dumps(data, indent=4))
    

# if request is unsuccessful, print error message
else:
    print("Error.", response.text)
