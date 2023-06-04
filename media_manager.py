import requests
import os
from dotenv import load_dotenv

tmdb_endpoint = "https://api.themoviedb.org/3"

# load environmental variables
load_dotenv()
key = os.environ.get("TMDB_TOKEN")
headers = {"accept": "application/json", "Authorization": key}

class MediaManager:
    """
    MediaManager searches for media details and stores relevant info as attributes.
    Info is retrieved using the consumet API.
    """

    def __init__(self):
        self.title = None
        self.poster = None
        self.media_type = None
        self.genres = None
        self.release_date = None
        self.language = None
        self.rating = None
        self.overview = None
        self.id = None


    def search_title(self, title):
        """
        Retrieves info on the given title search and assigns them as instance attributes.
        Search titles can be given in English or Japanese, but will return as Japanese.
        """

        response = requests.get(
        url=f"{tmdb_endpoint}/search/multi?query={title}", headers=headers)
        raw_data = response.json()

        # if response is unsuccessful, return none
        if response.status_code < 200 or response.status_code > 300:
            print("***ERROR*** ", response.text)
            return

        # if results is empty, return none
        elif not raw_data["results"]:
            print(f"No results for: '{title}'")
            return
        
        # set media details as attributes, note that movies and tv series have different labels for title and release date
        else:
            top_search = raw_data["results"][0]
            media_type = top_search["media_type"]

            if media_type == "tv":
                self.title = top_search["name"]
                self.release_date = top_search["first_air_date"]

            elif media_type == "movie":
                self.title = top_search["title"]
                self.release_date = top_search["release_date"]

            self.media_type = top_search["media_type"]

            genre_ids = top_search["genre_ids"]
            self.genres = self.translate_genre_ids(genre_ids)

            language_id = top_search["original_language"]
            self.language = self.translate_language_id(language_id)

            self.rating = top_search["vote_average"]
            self.id = top_search["id"]
            self.poster = f'https://image.tmdb.org/t/p/original{top_search["poster_path"]}'
            self.overview = top_search["overview"]


    def translate_genre_ids(self, ids):
        """
        Takes a list of genre IDs and returns a list of readable genre names.
        """
        genre_dicts = self.get_genre_dicts()

        # if no genre ids exist, return none
        if ids == None:
            return 
        
        # For each input id, loop through ref id dictionaries to find matching genre name
        else:
            genre_names = []
            for id in ids:
                for genre_dict in genre_dicts:
                    if genre_dict["id"] == id:
                        genre_name = genre_dict["name"]
                        genre_names.append(genre_name)

        return genre_names


    def get_genre_dicts(self):
        """
        Retrieves a list of all unique id,name dictionaries for both movie and tv shows.
        Uses the genre ID lists (movie, tv) from TMDB API.
        """

        # retrieve lgenre IDs from TMDB API and store as lists of dictionaries
        movie_response = requests.get(url=f"{tmdb_endpoint}/genre/movie/list", headers=headers)
        movie_ids = movie_response.json()["genres"]

        tv_response = requests.get(url=f"{tmdb_endpoint}/genre/tv/list", headers=headers)
        tv_ids = tv_response.json()["genres"]

        # combine movie and tv ID dictionaries into single list
        genre_ids = []

        for dict in movie_ids:
            if dict not in genre_ids:
                genre_ids.append(dict)

        for dict in tv_ids:
            if dict not in genre_ids:
                genre_ids.append(dict)

        return genre_ids
    
    
    def translate_language_id(self, id):
        """
        Retrieves the english name of a given language id.
        """

        response = requests.get(url=f"{tmdb_endpoint}/configuration/languages", headers=headers)
        language_dicts = response.json()

        for dict in language_dicts:
            if dict["iso_639_1"] == id:
                return dict["english_name"]
