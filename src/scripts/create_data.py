import os

from requests import delete

import create_train_data
import create_valid_from_data
from src.scripts.create_train_data import delete_all_images_from_folder, copy_images_to_train, \
    delete_whole_folder
from src.scripts.create_valid_from_data import select_and_move_images


def main():

    # Number of train and valid images for each brand.
    num_train_ims = 20
    num_valid_ims = 5
    brands = ["Alfa Romeo", "Bugatti", "Ferrari", "Porsche", "Tesla"]

    images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../images')
    train_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/train')
    valid_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/valid')

    # delete_all_images_from_folder(train_dir)
    delete_whole_folder(train_dir)
    # num_valid_ims will be moved later to valid folder
    copy_images_to_train(images_dir, train_dir, brands, num_train_ims + num_valid_ims)

    # delete_all_images_from_folder(valid_dir)
    delete_whole_folder(valid_dir)
    select_and_move_images(train_dir, valid_dir, brands, num_valid_ims)

if __name__ == '__main__':
    main()