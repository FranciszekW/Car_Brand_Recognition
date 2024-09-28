from filter_images import main as filter_images_main
from move_images import main as move_images_main
from reindex_data_images import main as reindex_main
from remove_image_duplicates import remove_from_data as remove_data_duplicates
from remove_image_duplicates import remove_from_raw as remove_raw_duplicates

def main():
    remove_raw_duplicates()
    filter_images_main()
    move_images_main()
    reindex_main()
    remove_data_duplicates()

if __name__ == "__main__":
    main()
