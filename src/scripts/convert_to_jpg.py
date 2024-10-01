import os
from PIL import Image


def convert_to_jpg(image_path):
    try:
        with Image.open(image_path) as img:
            # Convert the image to RGB to avoid issues with other formats
            img_rgb = img.convert("RGB")

            # Overwrite the image with the same name but saved as a proper JPG
            img_rgb.save(image_path, "JPEG")

            print(f"Converted {image_path} to JPG")
            return True
    except Exception as e:
        print(f"Error converting {image_path}: {e}")
        return False


# Main function to iterate through all images in a folder
def convert_folder_to_jpg(folder_path):
    for image_file in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_file)

        # Check if the file is an image (by extension)
        if image_file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            convert_to_jpg(image_path)


def main():
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data')

    # Convert all images in the folder and subfolders
    for brand in os.listdir(data_dir):
        brand_folder = os.path.join(data_dir, brand)
        if os.path.isdir(brand_folder):
            print(f"Formatting images from {brand} folder...")
            convert_folder_to_jpg(brand_folder)


if __name__ == "__main__":
    main()
