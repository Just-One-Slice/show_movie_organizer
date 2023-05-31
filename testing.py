import requests
import json

endpoint = "https://api.themoviedb.org/3/search/multi"
key = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYjg3MWUyOGJiMWNlYjVkMTI5ZWUzMTI0MTVhNmVmNCIsInN1YiI6IjY0NzUwMjIyYmJjYWUwMDBhODU5NDA5NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.uebm45xswSNm_tBcPPqGyxkwkdoE6YQj2ilF4gj36Ek"
title = "inception"

headers = {"accept": "application/json",
           "Authorization": key}

response = requests.get(url=f"{endpoint}?query={title}", headers=headers)
data = response.json()["results"]
print(json.dumps(data, indent=4))

# title = "Angel Beats"

# # if request is successful...
# if response.status_code >= 200 and response.status_code < 300:
#     data = response.json()["results"]
#     print(json.dumps(data, indent=4))


# # if request is unsuccessful, print error message
# else:
#     print("Error.", response.text)
