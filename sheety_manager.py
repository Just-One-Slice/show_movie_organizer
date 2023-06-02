import requests
import os
from dotenv import load_dotenv

# load environmental variables
load_dotenv()
key = os.environ.get("SHEETY_TOKEN")

class SheetyManager:
    """
    Manages media information to and from a Google sheet.
    Uses the Sheety API.
    """
    # TODO: set Sheety endpoints for GET and PUT, set as environmental variables
    
    pass
