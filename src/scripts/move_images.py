import os
import shutil

# Function to move images from raw_images to data and raise error on collisions
def move_images_with_collision_check(raw_images_dir, images_dir):
    # Iterate through each brand folder in the raw_images directory
    for brand in os.listdir(raw_images_dir):
        raw_brand_folder = os.path.join(raw_images_dir, brand)
        data_brand_folder = os.path.join(images_dir, brand)

        # Ensure we are dealing with directories
        if os.path.isdir(raw_brand_folder):
            # Check if the corresponding brand folder exists in the data directory
            if not os.path.exists(data_brand_folder):
                print(f"Creating brand folder in data: {data_brand_folder}")
                os.makedirs(data_brand_folder)

            # Iterate through the files in the raw brand folder
            for filename in os.listdir(raw_brand_folder):
                raw_image_path = os.path.join(raw_brand_folder, filename)
                data_image_path = os.path.join(data_brand_folder, filename)

                # Check if a file with the same name already exists in the destination
                if os.path.exists(data_image_path):
                    raise FileExistsError(f"File collision detected: {data_image_path} already exists!")

                # Move the file to the corresponding brand folder in the data directory
                print(f"Moving {raw_image_path} to {data_image_path}")
                shutil.move(raw_image_path, data_image_path)

        else:
            print(f"Skipping non-directory item in raw_images: {brand}")

# Main function to execute the moving process
def main():
    # Define the path to the data and raw_images directories
    raw_images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../raw_images')
    images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../images')

    # Move images and check for collisions
    move_images_with_collision_check(raw_images_dir, images_dir)

if __name__ == "__main__":
    main()
