# noinspection PyUnresolvedReferences
import matplotlib.pyplot as plt
from PIL import Image


def show_image(image_path):
    image = Image.open(image_path)
    plt.imshow(image)
    plt.show()


def prepare_image(image_path, device, pre_transforms):
    image = Image.open(image_path)
    image = pre_transforms(image)  # pretrained_weights.transforms()
    image = image.unsqueeze(0).to(device)  # create a batch for model
    return image
