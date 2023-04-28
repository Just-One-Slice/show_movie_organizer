import requests
import json

consumet_api_endpoint = "https://api.consumet.org/anime/gogoanime/"


class MediaManager:
    # attributes
    title = ""
    format = ""
    language = ""
    rating = None

    # name search
    def search_title(self, title):
        response = requests.get(
            url=f"{consumet_api_endpoint}{title}",
        )

        # if request is successful, print data
        if response.status_code >= 200 and response.status_code < 300:
            data = response.json()
            print(json.dumps(data, indent=4))
            return data

        # if request is unsuccessful, print error message
        else:
            print("Error.", response.text)
