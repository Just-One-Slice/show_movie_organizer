import requests
import json
import os
from dotenv import load_dotenv

endpoint = "https://api.themoviedb.org/3/configuration/languages"
load_dotenv()
key = os.environ.get("TMDB_TOKEN")

headers = {"accept": "application/json",
           "Authorization": key}

response = requests.get(url=f"{endpoint}", headers=headers)
data = response.json()
print(data)


# title = "Angel Beats"

# # if request is successful...
# if response.status_code >= 200 and response.status_code < 300:
#     data = response.json()["results"]
#     print(json.dumps(data, indent=4))


# # if request is unsuccessful, print error message
# else:
#     print("Error.", response.text)
