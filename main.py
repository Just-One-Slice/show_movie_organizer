# takes in show and movie titles and inserts relevant meta data
# (ex. genre, release date, rating, language)

import requests

from media_manager import MediaManager


# # read titles from sheety
# sheety_endpoint = "https://api.sheety.co/3d79b938ab89d5e0f4ee389d338c0bb6/mediaList/media"

# sheety_response = requests.get(
#     url=sheety_endpoint
# )

# data = sheety_response.json()

# print(sheety_response.status_code)
# print(sheety_response.text)


# search for anime info
media_manager = MediaManager()
title = "Pokemon"
media_manager.search_anime(title)

print(f"""
Title: {media_manager.title}
Genres: {media_manager.genres}
Episodes: {media_manager.episodes}
Status: {media_manager.status}
Release Date: {media_manager.release_date}
""")
