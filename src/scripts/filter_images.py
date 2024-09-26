import os
import cv2


def view_and_delete_images(image_folder):
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


# Example usage:
if __name__ == "__main__":
    image_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../raw_images/Alfa Romeo')
    view_and_delete_images(image_folder)
