"""
Takes in show and movie titles from a Google sheet. 
Automatically fills in relevant media info (ex. genre, release date, rating, language).
"""

from sheety_manager import SheetyManager

# create SheetyManager class
sheety_manager = SheetyManager()

# NOTE: For non-English films, set the search title in the original language
sheety_manager.fill_empty_rows()
