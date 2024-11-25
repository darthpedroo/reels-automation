import os
import requests
from dotenv import load_dotenv
from instagrapi import Client

load_dotenv()

ACCESS_TOKEN = os.getenv("INSTA_TOKEN_PERSONAJE")
ENDPOINT = "https://graph.instagram.com/me"

# Parameters for the request
params = {
    "fields": "id,username,account_type",
    "access_token": ACCESS_TOKEN
}

try:
    response = requests.get(ENDPOINT, params=params)
    data = response.json()

    # Print response
    if "error" in data:
        print("Error:", data["error"]["message"])
    else:
        print("User Info:", data)

except Exception as e:
    print("An error occurred:", str(e))
