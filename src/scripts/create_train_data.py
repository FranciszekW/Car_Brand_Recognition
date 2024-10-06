import os
import shutil
import random
from glob import glob

def delete_all_images_from_train(train_dir):
    # Iterate over each brand directory in the train folder
    for brand_dir in os.listdir(train_dir):
        brand_train_dir = os.path.join(train_dir, brand_dir)

        if os.path.isdir(brand_train_dir):
            # Get all .jpg images in the brand directory
            images = glob(os.path.join(brand_train_dir, "*.jpg"))

            # Delete each image found
            for img_path in images:
                os.remove(img_path)

            print(f"Deleted all images in: {brand_train_dir}")

def copy_images_to_train(images_dir, train_dir, num_ims):
    # Ensure the target train directory exists
    os.makedirs(train_dir, exist_ok=True)

    # Iterate over each brand directory in the images folder
    for brand_dir in os.listdir(images_dir):
        brand_images_dir = os.path.join(images_dir, brand_dir)
        train_brand_dir = os.path.join(train_dir, brand_dir)

        if os.path.isdir(brand_images_dir):
            # Ensure the train brand folder exists
            os.makedirs(train_brand_dir, exist_ok=True)

            # Get all .jpg images in the brand directory
            images = glob(os.path.join(brand_images_dir, "*.jpg"))

            # Randomly select num_samples images (or fewer if not enough images are available)
            selected_images = random.sample(images, min(num_ims, len(images)))

            # Copy the first 'num_ims' images to the train folder
            for img_path in selected_images:
                shutil.copy(img_path, train_brand_dir)

    print(f"Copied {num_ims} images per brand to the train directory.")

def main():
    # Directories relative to the script's location
    images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../images')
    train_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/train')

    # Set the number of images to copy for each brand
    num_ims = 30  # adjust the number as needed

    # Delete all images before copying
    delete_all_images_from_train(train_dir)

    # Call the function to copy images
    copy_images_to_train(images_dir, train_dir, num_ims)

if __name__ == "__main__":
    main()
