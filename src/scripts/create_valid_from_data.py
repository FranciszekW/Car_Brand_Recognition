import os
import random
import shutil

def select_and_move_images(data_folder, validate_folder, num_images=10):
    # Ensure the validate folder exists
    if not os.path.exists(validate_folder):
        os.makedirs(validate_folder)

    # Loop through each brand folder in the data directory
    for brand in os.listdir(data_folder):
        brand_folder = os.path.join(data_folder, brand)

        # Check if the path is a directory (brand folder)
        if os.path.isdir(brand_folder):
            # Get the list of images in the brand folder
            images = [img for img in os.listdir(brand_folder) if img.endswith('.jpg')]

            # Select 10 images (randomly if needed)
            selected_images = random.sample(images, min(num_images, len(images)))

            # Ensure the brand folder exists in the validate folder
            validate_brand_folder = os.path.join(validate_folder, brand)
            if not os.path.exists(validate_brand_folder):
                os.makedirs(validate_brand_folder)

            # Move selected images to the validate brand folder
            for img in selected_images:
                src_path = os.path.join(brand_folder, img)
                dst_path = os.path.join(validate_brand_folder, img)
                shutil.move(src_path, dst_path)

            print(f"Moved {len(selected_images)} images for brand: {brand}")

def main():
    data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data')
    train_folder = os.path.join(data_folder, 'train')
    validate_folder = os.path.join(data_folder, 'valid')
    select_and_move_images(train_folder, validate_folder, num_images=10)

if __name__ == '__main__':
    main()