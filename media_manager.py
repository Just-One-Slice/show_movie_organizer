import requests
import json


class MediaManager:
    """
    MediaManager searches for media details and stores relevant info as attributes.
    Info is retrieved using the consumet API.
    """

    def __init__(self):
        self.title = None
        self.media_type = None
        self.genres = None
        self.release_date = None
        self.language = None
        self.id = None

    def search_title(self, title):
        """
        Retrieves info on the given title search and assigns them as instance attributes.
        Search titles can be given in English or Japanese, but will return as Japanese.
        """

        tmdb_endpoint = "https://api.themoviedb.org/3/search"
        key = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYjg3MWUyOGJiMWNlYjVkMTI5ZWUzMTI0MTVhNmVmNCIsInN1YiI6IjY0NzUwMjIyYmJjYWUwMDBhODU5NDA5NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.uebm45xswSNm_tBcPPqGyxkwkdoE6YQj2ilF4gj36Ek"

        headers = {"accept": "application/json", "Authorization": key}

        response = requests.get(url=f"{tmdb_endpoint}/multi?query={title}", headers=headers)
        raw_data = response.json()

        # if response is unsuccessful, return none
        if response.status_code < 200 or response.status_code > 300:
            print("***ERROR*** ", response.text)
            return

        # if results is empty, return none
        if not raw_data["results"]:
            print(f"No results for: '{title}'")
            return
        
        # set media details as attributes
        else:
            top_search = raw_data["results"][0]
            
            self.title = top_search["name"]
            self.media_type = top_search["media_type"]
            self.genres = top_search["genre_ids"]
            self.release_date = top_search["first_air_date"]
            self.language = top_search["original_language"]
            self.id = top_search["id"]

            
