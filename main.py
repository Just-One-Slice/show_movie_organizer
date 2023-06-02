# takes in show and movie titles and inserts relevant meta data
# (ex. genre, release date, rating, language)

from media_manager import MediaManager

# search for media info
media_manager = MediaManager()

# NOTE: For non-Japanese foreign films, set the search title to the original language
title = "킹덤"
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
