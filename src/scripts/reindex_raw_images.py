import os
import re
from download_images import get_last_index

# Function to rename files in raw_images based on the last index from data folder
def rename_files_in_raw_images(data_brand_folder, raw_brand_folder):
    # Get the last index from the data folder
    last_index = get_last_index(data_brand_folder)
    print(f"Last index in {data_brand_folder}: {last_index}")

    # First, rename files to a temporary name to avoid collisions
    temp_rename_map = []  # Track temp filenames for later renaming

    # Step 1: Temporary renaming
    for filename in os.listdir(raw_brand_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            last_index += 1  # Increment the index for each new file
            _, extension = os.path.splitext(filename)
            temp_filename = f"temp_{last_index}{extension}"

            old_file_path = os.path.join(raw_brand_folder, filename)
            temp_file_path = os.path.join(raw_brand_folder, temp_filename)

            print(f"Temporarily renaming {old_file_path} to {temp_file_path}")
            os.rename(old_file_path, temp_file_path)

            temp_rename_map.append((temp_file_path, f"image_{last_index}{extension}"))

    # Step 2: Final renaming to avoid collisions
    for temp_path, final_name in temp_rename_map:
        final_path = os.path.join(raw_brand_folder, final_name)
        print(f"Renaming {temp_path} to {final_path}")
        os.rename(temp_path, final_path)

# Main function to iterate through brand folders and rename files in raw_images
def main():
    # Define the path to the data and raw_images directories
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data')
    raw_images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../raw_images')

    # Iterate through each brand folder in the data directory
    for brand in os.listdir(data_dir):
        data_brand_folder = os.path.join(data_dir, brand)
        raw_brand_folder = os.path.join(raw_images_dir, brand)

        # Check if the brand folder exists in both data and raw_images
        if os.path.isdir(data_brand_folder) and os.path.isdir(raw_brand_folder):
            print(f"Reindexing raw images from: {brand}")
            # Rename the files in the raw_images/brand folder
            rename_files_in_raw_images(data_brand_folder, raw_brand_folder)
        else:
            print(f"Brand folder not found in either data or raw_images for {brand}")

if __name__ == "__main__":
    main()