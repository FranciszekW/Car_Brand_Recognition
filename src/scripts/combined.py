from filter_images import main as filter_images_main
from move_images import main as move_images_main
from reindex_data_images import main as reindex_main
from remove_image_duplicates import main as remove_duplicates_main

def main():
    filter_images_main()
    move_images_main()
    reindex_main()
    remove_duplicates_main()

if __name__ == "__main__":
    main()
