import requests
import json

consumet_api_endpoint = "https://api.consumet.org/anime/gogoanime"


class MediaManager:
    def __init__(self):
        self.title = None
        self.genres = None
        self.episodes = None
        self.status = None
        self.release_date = None
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
            earliest_date = 9999

            for row in raw_data:
                try:
                    new_date_str = row["releaseDate"].split(" ")[-1]

                # ignore empty strings
                except ValueError:
                    print("invalid date")

                else:
                    new_date = int(new_date_str)

                    # if new date is earlier, set as release date
                    if new_date < earliest_date:
                        earliest_date = new_date
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

            self.title = data["title"]
            self.genres = data["genres"]
            self.episodes = data["totalEpisodes"]
            self.status = data["status"]
            self.release_date = data["releaseDate"]

        else:
            print("Error.", response.text)
