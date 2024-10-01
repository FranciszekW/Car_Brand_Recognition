import os
import cv2


def view_and_delete_images_in_folder(image_folder):
    for filename in os.listdir(image_folder):
        if filename.endswith(
                (".jpg", ".jpeg", ".png", ".gif")):  # Include image formats you want to process
            image_path = os.path.join(image_folder, filename)
            image = cv2.imread(image_path)

            if image is None:
                print(f"Failed to load {filename}")
                continue

            # Display the image in a window
            cv2.imshow("Image Viewer", image)
            print(f"Viewing {filename}. Press 'd' to delete, any other key to keep.")

            # Wait for a key press
            key = cv2.waitKey(0)

            if key == ord('d'):
                print(f"Deleting {filename}...")
                os.remove(image_path)
            else:
                print(f"Keeping {filename}.")

            # Close the window
            cv2.destroyAllWindows()

    print("Finished processing all images.")

def process_brand_folders(raw_images_folder):
    """
    Function to iterate through each brand folder and apply the image deletion logic.
    """
    for brand_folder in sorted(os.listdir(raw_images_folder)):
        brand_folder_path = os.path.join(raw_images_folder, brand_folder)
        if os.path.isdir(brand_folder_path):  # Ensure it's a directory
            print(f"Filtering images from brand: {brand_folder}")
            view_and_delete_images_in_folder(brand_folder_path)

def main():
    image_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../raw_images')
    process_brand_folders(image_folder)

if __name__ == "__main__":
    main()
