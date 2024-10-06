from manually_filter_images import main as filter_images_main
from move_images import main as move_images_main
from reindex_data_images import main as reindex_main
from reindex_raw_images import  main as reindex_raw
from remove_image_duplicates import remove_from_images as remove_images_duplicates
from remove_image_duplicates import remove_from_raw as remove_raw_duplicates
from remove_corrupted_images import main as remove_corrupted_images

def main():
    remove_raw_duplicates()
    reindex_raw()
    filter_images_main()
    move_images_main()
    reindex_main()
    remove_corrupted_images()
    remove_images_duplicates()

if __name__ == "__main__":
    main()
