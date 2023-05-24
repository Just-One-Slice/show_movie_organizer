import requests
import json

consumet_api_endpoint = "https://api.consumet.org/anime/gogoanime"


class MediaManager:
    """
    MediaManager searches for media id's and stores relevant media info as attributes.
    Info is retrieved using the consumet API.
    """

    def __init__(self):
        self.title = None
        self.genres = None
        self.episodes = None
        self.status = None
        self.release_date = None
        self.id = None

    def search_title(self, title):
        """
        Retrieves the id of the earliest release of a given anime title.
        Search titles can be given in English or Japanese, but will return as Japanese.
        """
        response = requests.get(url=f"{consumet_api_endpoint}/{title}")
        raw_data = response.json()["results"]

        # if response is unsuccessful, return none
        if response.status_code < 200 or response.status_code > 300:
            print("***ERROR*** ", response.text)
            return

        # if no results returned, return none
        if not raw_data:
            print(f"No results for: {title}")
            return

        # if request is successful, extract release dates of each dictionary
        else:
            earliest_movie = None
            earliest_date = 9999

            for row in raw_data:
                # if releaseDate field is empty, continue to next row
                if row["releaseDate"] == "":
                    continue

                # extract year as string
                new_date_str = row["releaseDate"].split(":")[-1].strip()
                new_date = int(new_date_str)

                # if new date is earlier, set as release date
                if new_date < earliest_date:
                    earliest_date = new_date
                    earliest_movie = row

            id = earliest_movie["id"]
            return id

    def get_info(self, id):
        """
        Returns relevant info from a given anime id
        """
        response = requests.get(f"{consumet_api_endpoint}/info/{id}")
        data = response.json()

        self.title = data["title"]
        self.genres = data["genres"]
        self.episodes = data["totalEpisodes"]
        self.status = data["status"]
        self.release_date = data["releaseDate"]
