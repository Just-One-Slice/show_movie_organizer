import requests
import json

consumet_api_endpoint = "https://api.consumet.org/anime/gogoanime"


class MediaManager:
    def __init__(self):
        self.title = None
        self.genres = None
        self.episodes = None
        self.status = None
        self.release_date = 9999
        self.id = None

    # retrieves the id of the earliest release of a given search title
    def search_title(self, title):
        response = requests.get(url=f"{consumet_api_endpoint}/{title}")

        # if request is successful...
        if response.status_code >= 200 and response.status_code < 300:
            raw_data = response.json()["results"]

            # extract release dates of each dictionary
            # TODO: create exception to skip empty releaseDate fields

            earliest_movie = None
            
            for row in raw_data:
                try:
                    new_date_str = row["releaseDate"].split(" ")[-1]

                # ignore empty strings
                except ValueError:
                    print("invalid date")

                else:
                    new_date = int(new_date_str)

                    #if new date is earlier, set as release date
                    if new_date < MediaManager.release_date:
                        MediaManager.release_date = new_date
                        earliest_movie = row

            id = earliest_movie["id"]
            return id

        # if request is unsuccessful, print error message
        else:
            print("Error.", response.text)


    # request meta data about title
    def get_info(self, id):
        response = requests.get(f"{consumet_api_endpoint}/info/{id}")

        if response.status_code >= 200 and response.status_code < 300:
            data = response.json()

            MediaManager.title = data["title"]
            MediaManager.genres = data["genres"]
            MediaManager.episodes = data["totalEpisodes"]
            MediaManager.status = data["status"]

        else:
            print("Error.", response.text)