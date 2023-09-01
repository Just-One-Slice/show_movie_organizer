import requests
import os
import json
from dotenv import load_dotenv
from media_manager import MediaManager

# load environmental variables
load_dotenv()
sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
sheety_token = os.environ.get("SHEETY_TOKEN")
headers = {"Content-Type": "application/json",
           "Authorization": sheety_token}


class SheetyManager:
    """
    Manages media information to and from a Google sheet using the Sheety API.
    The sheet should be formatted with the following headers:
        "title", "alternateTitle", "poster", "mediaType", "genre", "releaseDate, language, rating, overview", "|"
    NOTE:   All data-containing rows must have the "|" character under the "|" column at the farthest right cell.
            This allows the API to read null values in the row.
    """

    def fill_empty_rows(self):
        """
        Reads and fills all rows containing only titles with corresponding media info.
        """

        response = requests.get(url=sheety_endpoint, headers=headers)

        # return error if response is unsuccessful
        if response.status_code < 200 or response.status_code > 300:
            print(f"ERROR {response.status_code}. {response.text}")
            return

        else:
            data = response.json()["medias"]

            # loop through all rows without posters
            for row in data:
                if row["poster"] == "":
                    # if alternate title exists, set as title
                    if row["alternateTitle"] != "":
                        title = row["alternateTitle"]
                    # otherise use title
                    else:
                        title = row["title"]
                    row_id = row["id"]
                    self.edit_row(row_id, title)

                else:
                    continue

    def edit_row(self, row, title):
        """
        Sends a PUT request to edit a specific row within the sheet.
        Row input is equivalent to the row number in the sheet (eq. 1 = Headers)
        """

        payload = self.create_payload(title)
        response = requests.put(url=f"{sheety_endpoint}/{row}",
                                headers=headers,
                                json=payload)

        if response.status_code < 200 or response.status_code > 300:
            print("***ERROR*** ", response.text)
            return

        else:
            print("PUT request successful. ", response.text)

    def create_payload(self, title):
        """
        Creates a JSON payload from MediaManager and puts to the Sheety API.
        Payload must be nested in a singular root property named after the sheet name (eq. media).
        Headers in the sheet are read as camelCase (eq. mediaType).
        Values must be typed as str, int, or float
        """

        media_manager = MediaManager()
        media_manager.search_title(title)

        # Structure JSON payload, convert values to str
        payload = {
            "media": {
                "title": f"{media_manager.title}",
                "poster": f"{media_manager.poster}",
                "link": f"{media_manager.link}",
                "mediaType": f"{media_manager.media_type.capitalize()}",
                "genre": f"{', '.join(media_manager.genres)}",
                "releaseDate": f"{media_manager.release_date}",
                "language": f"{media_manager.language}",
                "rating": f"{media_manager.rating}",
                "overview": f"{media_manager.overview}"
            }
        }

        return payload
