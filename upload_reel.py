import os
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ADMIN_APP_TOKEN")
VIDEO_URL = "El impacto de los wireframes y prototipos en el diseño de aplicaciones_RVC_1.mp4"  # The URL of the video you want to upload
CAPTION = "Your caption for the reel here!"

# Step 1: Fetch the Facebook Page ID and Instagram Business Account ID
def get_instagram_account_id():
    # Request to get the user's Facebook pages
    pages_endpoint = "https://graph.facebook.com/v21.0/me/accounts"
    params = {
        "access_token": ACCESS_TOKEN
    }

    response = requests.get(pages_endpoint, params=params)
    data = response.json()
    print("DATA", data)
    if "data" in data:
        for page in data["data"]:
            page_id = page["id"]
            print(f"Page ID: {page_id}")

            # Use the page ID to fetch the Instagram Business Account ID
            instagram_endpoint = f"https://graph.facebook.com/v17.0/{page_id}?fields=instagram_business_account&access_token={ACCESS_TOKEN}"
            instagram_response = requests.get(instagram_endpoint)
            instagram_data = instagram_response.json()

            if "instagram_business_account" in instagram_data:
                instagram_account_id = instagram_data["instagram_business_account"]["id"]
                print(f"Instagram Account ID: {instagram_account_id}")
                return instagram_account_id
            else:
                print("No Instagram Business Account found for this page.")
    else:
        print("Error fetching pages:", data)

    return None

# Step 2: Upload video to the container
def upload_video_to_container(instagram_account_id):
    media_endpoint = f"https://graph.facebook.com/v17.0/{instagram_account_id}/media"
    
    params = {
        "access_token": ACCESS_TOKEN,
        "media_type": "VIDEO",
        "video_url": VIDEO_URL,  # The video must be hosted and publicly accessible
        "caption": CAPTION,
        "share_to_feed": True  # Set True to also share it to the feed
    }
    
    response = requests.post(media_endpoint, params=params)
    data = response.json()
    
    if "id" in data:
        print(f"Media container created successfully! ID: {data['id']}")
        return data["id"]  # The container ID
    else:
        print("Error while creating media container:", data)
        return None

# Step 3: Publish the media container
def publish_video(container_id, instagram_account_id):
    publish_endpoint = f"https://graph.facebook.com/v17.0/{instagram_account_id}/media_publish"
    
    params = {
        "access_token": ACCESS_TOKEN,
        "creation_id": container_id
    }
    
    response = requests.post(publish_endpoint, params=params)
    data = response.json()
    
    if "id" in data:
        print(f"Reel published successfully! Media ID: {data['id']}")
    else:
        print("Error while publishing reel:", data)

# Main workflow
if __name__ == "__main__":
    print("Fetching Instagram account ID...")
    instagram_account_id = get_instagram_account_id()

    print(instagram_account_id)
    
    if instagram_account_id:
        print("Uploading video to Instagram...")
        container_id = upload_video_to_container(instagram_account_id)
        
        if container_id:
            print("Publishing reel...")
            publish_video(container_id, instagram_account_id)
