import requests
import json
import os
from dotenv import load_dotenv
from media_manager import MediaManager
from sheety_manager import SheetyManager

# # returns row in google sheet
# load_dotenv()
# sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
# sheety_token = os.environ.get("SHEETY_TOKEN")
# headers = {"Content-Type": "application/json",
#            "Authorization": sheety_token}

# response = requests.get(url=sheety_endpoint, headers=headers)
# data = response.json()["medias"][35]

# print(json.dumps(data, indent=3))


# returns media data for a given title
media_manager = MediaManager()
title = "Avatar: The Last Airbender"
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
Overview: {media_manager.overview}
""")
