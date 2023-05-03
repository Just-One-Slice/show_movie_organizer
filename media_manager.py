import requests
import json

consumet_api_endpoint = "https://api.consumet.org/anime/gogoanime"


class MediaManager:
    # attributes
    title = ""
    format = ""
    language = ""
    release_date = 9999
    rating = None

    # name search
    def search_title(self, title):
        response = requests.get(url=f"{consumet_api_endpoint}/{title}")

        # if request is successful...
        if response.status_code >= 200 and response.status_code < 300:
            raw_data = response.json()["results"]

            # extract release dates of each dictionary
            # TODO: create exception to skip empty releaseDate fields
            for row in raw_data:
                try:
                    new_date_str = row["releaseDate"].split(" ")[-1]

                # ignore empty strings
                except ValueError:
                    print("invalid date")

                else:
                    new_date = int(new_date_str)

                    #if new date is earlier, set as release date
                    if new_date < MediaManager.release_date:
                        MediaManager.release_date = new_date
                    
            print(MediaManager.release_date)


            # # return id of first dictionary with earlist release date
            # for row in raw_data:
            #     try: 
            #         new_date_str = row["releaseDate"].split(" ")[-1]
                
            #     # ignore empty strings
            #     except ValueError:
            #         print("invalid date")

            #     else:
            #         if str(MediaManager.release_date) in row["releaseDate"]:
            #             return row

        # if request is unsuccessful, print error message
        else:
            print("Error.", response.text)


    # request meta data about title
    def get_info(self, id):
        response = requests.get(f"{consumet_api_endpoint}/info/{id}")

        if response.status_code >= 200 and response.status_code < 300:
            data = response.json()
            print(json.dumps(data, indent=4))
            return data

        else:
            print("Error.", response.text)