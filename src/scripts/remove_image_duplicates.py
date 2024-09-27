import os
from PIL import Image
import imagehash
import shutil


# Function to calculate image hash
def calculate_hash(image_path):
    try:
        with Image.open(image_path) as img:
            return imagehash.phash(img)
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

# Function to resize an image to the target size
def resize_image(image_path, target_size):
    try:
        with Image.open(image_path) as img:
            resized_img = img.resize(target_size)
            return resized_img
    except Exception as e:
        print(f"Error resizing {image_path}: {e}")
        return None

# Function to remove duplicates in a brand folder
def remove_duplicates(brand_folder, threshold=3):
    image_hashes = {}
    removed_images = 0

    for image_file in os.listdir(brand_folder):
        if image_file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image_path = os.path.join(brand_folder, image_file)
            image_hash = calculate_hash(image_path)

            if image_hash:
                for existing_hash, existing_file in image_hashes.items():
                    hash_diff = image_hash - existing_hash
                    print(f"Hash difference between {image_file} and {existing_file}: {hash_diff}")
                    # if hash_diff < threshold:
                    #     print(f"Removing duplicate: {image_file} (similar to {existing_file})")
                    #     os.remove(image_path)
                    #     removed_images += 1
                    #     break
                else:
                    image_hashes[image_hash] = image_file

    print(f"Removed {removed_images} duplicate images from {brand_folder}")

# Main function to iterate through brand folders in data directory
def main():
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data')
    # Iterate through each brand folder
    for brand in os.listdir(data_dir):
        brand_folder = os.path.join(data_dir, brand)
        if os.path.isdir(brand_folder):
            print(f"Processing {brand} folder...")
            remove_duplicates(brand_folder)

if __name__ == "__main__":
    main()