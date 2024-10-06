import os
from PIL import Image

# Function to check if an image can be opened and converted to JPG
def is_valid_image(image_path):
    try:
        with Image.open(image_path) as img:
            # It does NOT change the original image.
            img.convert("RGB")  # Try to convert the image to JPG format (RGB)
        return True
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return False

# Function to remove corrupted images in a folder
def remove_corrupted_images(folder_path):
    removed_images = 0

    for image_file in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_file)
        if image_file.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            if not is_valid_image(image_path):
                print(f"Removing corrupted image: {image_file}")
                os.remove(image_path)
                removed_images += 1

    print(f"Removed {removed_images} corrupted images from {folder_path}")

# Main function to iterate through brand folders in data directory
def main():
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../images')

    # Iterate through each brand folder
    for brand in os.listdir(data_dir):
        brand_folder = os.path.join(data_dir, brand)
        if os.path.isdir(brand_folder):
            print(f"Removing corrupted images from {brand} folder...")
            remove_corrupted_images(brand_folder)

if __name__ == "__main__":
    main()