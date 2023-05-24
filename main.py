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


# search for title ID
media_manager = MediaManager()
title = "code geass"

# TODO: merge get_info() method into search_title() so only one method call is needed
id = media_manager.search_title(title)

# get info of ID
media_manager.get_info(id)

print(f"""
Title: {media_manager.title}
Genres: {media_manager.genres}
Episodes: {media_manager.episodes}
Status: {media_manager.status}
Release Date: {media_manager.release_date}
""")
