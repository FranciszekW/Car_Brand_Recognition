#%%
import re
import requests
import os
import time
from requests.exceptions import Timeout, RequestException
from PIL import Image
from io import BytesIO


# %%
# Function to perform Google Custom Search for images
def google_image_search(api_key, search_engine_id, query, start_index, num_images=100):
    url = "https://www.googleapis.com/customsearch/v1"
    image_urls = []

    while len(image_urls) < num_images:
        params = {
            'key': api_key,
            'cx': search_engine_id,
            'q': query,
            'searchType': 'image',
            'num': 10,  # Max number of results per request
            'start': start_index,
        }

        response = requests.get(url, params=params)
        data = response.json()

        if 'items' not in data:
            print("No more results found.")
            break

        for item in data['items']:
            image_urls.append(item['link'])
            if len(image_urls) >= num_images:
                break

        start_index += 10  # Move to the next set of images
        time.sleep(1)  # Avoid hitting API rate limits

    return image_urls


# %%
# Function to download images without conversion
def download_images(image_urls, folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for index, url in enumerate(image_urls):
        attempts = 0
        success = False

        while attempts < 3 and not success:  # Retry up to 3 times
            try:
                print(f"Downloading image {index + 1} from {url}")
                response = requests.get(url, timeout=10)  # Increased timeout
                response.raise_for_status()  # Raise an error for bad responses
                # Save the image as is
                image_path = os.path.join(folder_name, f"image_{index + 1}.jpg")
                with open(image_path, 'wb') as file:
                    file.write(response.content)
                print(f"Downloaded {image_path}")
                success = True  # Mark as successful
            except Timeout:
                attempts += 1
                print(
                    f"Timeout occurred while trying to download {url}. Retrying... ({attempts}/3)")
                time.sleep(1)  # Wait a bit before retrying
            except RequestException as e:
                print(f"Error downloading image {index + 1} from {url}: {e}")
                break  # Break on other request exceptions

        time.sleep(0.3)  # Slight delay to avoid overwhelming the server
#%%
def get_last_index(folder_name):
    max_index = -1  # Start with -1 to handle empty folders
    try:
        for filename in os.listdir(folder_name):
            # Match "image_X" where X is the index, ignore the extension
            match = re.search(r'image_(\d+)', filename)
            if match:
                index = int(match.group(1))
                max_index = max(max_index, index)
    except FileNotFoundError:
        pass  # If the folder doesn't exist, return -1

    return max_index
# %%
# Main process to iterate through the Car_brands directory
def main():
    api_key = "AIzaSyDvIRsZu12SY7i8unJcT0jzqx39QrbeH_o"
    search_engine_id = "8739bdf9e17c54c1b"

    # Path to the Car_brands directory (relative to the current script directory)
    car_brands_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data')

    # Define the images directory path
    images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'../raw_images')

    # Iterate through the folders (brand names) in the data directory
    for brand in os.listdir(car_brands_dir):
        brand_path = os.path.join(car_brands_dir, brand)

        # Check if the item is a directory (brand folder)
        if os.path.isdir(brand_path):
            query = f"{brand} car"  # Construct the search query
            print(f"Searching for images of {query}...")

            # Determine the last index of downloaded images
            brand_image_path = os.path.join(car_brands_dir, brand)
            save_to_path = os.path.join(images_dir, brand)
            last_index = get_last_index(brand_image_path)  # Get the last index from existing images
            print(f"Last downloaded index for {brand}: {last_index}")
            # Search for images starting from the last index
            try:
                image_urls = google_image_search(api_key, search_engine_id, query,
                                                 start_index=last_index + 1, num_images=200)

                # Download images directly into the corresponding brand's folder
                download_images(image_urls, folder_name=save_to_path)
            except Exception as e:
                print(f"Error processing brand {brand}: {e}")

            time.sleep(2)  # Add a delay between brand requests to avoid hitting API limits


# %%
if __name__ == "__main__":
    main()
