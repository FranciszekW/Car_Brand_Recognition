import os
import re


def rename_images_sequentially(folder_path):
    """
    Rename images in a folder so that their indices are 0, 1, 2, ..., without gaps.
    """
    # Create a list to store the image file paths
    image_files = []

    # List all files in the folder and filter only image files (e.g., .jpg, .jpeg, .png)
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image_files.append(filename)

    # Sort the image files based on the current indices in their names
    # Assuming the filenames are in the format: 'image_x.extension'
    image_files.sort(key=lambda f: int(re.search(r'image_(\d+)', f).group(1)))

    # Rename each image sequentially
    for new_index, old_filename in enumerate(image_files):
        # Extract the file extension
        _, file_extension = os.path.splitext(old_filename)

        # Define the new filename
        new_filename = f"image_{new_index}{file_extension}"

        # Construct full paths for the old and new filenames
        old_file_path = os.path.join(folder_path, old_filename)
        new_file_path = os.path.join(folder_path, new_filename)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {old_filename} to {new_filename}")

    print(f"Renamed all images in folder: {folder_path}")


def process_all_brands(dir):
    """
    Iterate through every brand folder in the data directory and rename images sequentially.
    """
    # Iterate through each folder in the data directory
    for brand_folder in os.listdir(dir):
        brand_folder_path = os.path.join(dir, brand_folder)

        # Check if the item is a directory (brand folder)
        if os.path.isdir(brand_folder_path):
            print(f"Reindexing images from: {brand_folder}")
            rename_images_sequentially(brand_folder_path)

def main():
    # Path to the data directory (contains brand folders)
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../images')

    # Call the function to process all brand folders
    process_all_brands(data_dir)

if __name__ == "__main__":
    main()
