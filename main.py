# takes in show and movie titles and inserts relevant meta data
# (ex. genre, release date, rating, language)

from media_manager import MediaManager
import json

# # read titles from sheety
# sheety_endpoint = "https://api.sheety.co/3d79b938ab89d5e0f4ee389d338c0bb6/media_managerList/media_manager"

# sheety_response = requests.get(
#     url=sheety_endpoint
# )

# data = sheety_response.json()

# print(sheety_response.status_code)
# print(sheety_response.text)


# search for anime info
media_manager = MediaManager()
title = "Grand Budapest Hotel"
media_manager.search_title(title)

print(f"""
Title: {media_manager.title}
Type: {media_manager.media_type}
Genres: {media_manager.genres}
Release Date: {media_manager.release_date}
Language: {media_manager.language}
Rating: {media_manager.rating}
ID: {media_manager.id}
Poster: {media_manager.poster}
""")
