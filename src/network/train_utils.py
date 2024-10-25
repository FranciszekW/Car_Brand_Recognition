import os
import glob
from PIL import Image
# noinspection PyUnresolvedReferences
import torch
# noinspection PyUnresolvedReferences
from torch.utils.data import Dataset
import image_utils


def count_folders(directory):
    # List all items in the directory and filter for folders
    folder_count = sum(
        1 for item in os.listdir(directory) if os.path.isdir(os.path.join(directory, item)))
    return folder_count


class DatasetFromFolders(Dataset):
    def __init__(self, data_dir, data_labels, device, pre_transforms=None):
        self.data_dir = data_dir
        self.pre_transforms = pre_transforms
        self.images = []
        self.labels = []

        # Load images and labels into memory
        for label_index, label in enumerate(data_labels):
            data_paths = glob.glob(data_dir + label + '/*.jpg', recursive=True)
            for path in data_paths:
                image = Image.open(path)
                self.images.append(pre_transforms(image).to(device))
                self.labels.append(torch.tensor(label_index).to(device).long())

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        return self.images[idx], self.labels[idx]


# We divide the number of correct guesses by the size of whole dataset. This is strange,
# but allows us to sum the accuracies later instead of than dividing them again.
def batch_accuracy(output, y, dataset_size):
    prediction = output.argmax(dim=1, keepdim=True)
    num_correct = prediction.eq(y.view_as(prediction)).sum()
    num_correct = num_correct.item() # convert from tensor to number
    return num_correct / dataset_size


def train_and_valid(model, train_loader, valid_loader, data_augment, optimizer, lr_scheduler,
                    loss_function, num_epochs):
    train_dataset_size = len(train_loader.dataset)
    valid_dataset_size = len(valid_loader.dataset)

    for epoch in range(num_epochs):
        print(f'Epoch {epoch + 1}/{num_epochs}, learning rate: {lr_scheduler.get_last_lr()[0]}')

        # Training:
        model.train()
        train_loss = 0
        train_accuracy = 0
        for x, y in train_loader:
            optimizer.zero_grad()
            output = model(data_augment(x))
            batch_loss = loss_function(output, y)
            batch_loss.backward()
            optimizer.step()

            train_loss += batch_loss.item()
            train_accuracy += batch_accuracy(output, y, train_dataset_size)
        print(f'Train: loss = {train_loss:.3f}, accuracy = {train_accuracy:.5f}')

        # Validation:
        model.eval()
        valid_loss = 0
        valid_accuracy = 0
        with torch.no_grad():
            for x, y in valid_loader:
                output = model(x)
                batch_loss = loss_function(output, y)

                valid_loss += batch_loss.item()
                valid_accuracy += batch_accuracy(output, y, valid_dataset_size)
            print(f'Valid: loss = {valid_loss:.3f}, accuracy = {valid_accuracy:.5f}\n')

        lr_scheduler.step(valid_loss)

def model_prediction(model, data_labels, image_path, device, pre_transforms):
    image_utils.show_image(image_path)

    image = image_utils.prepare_image(image_path, device, pre_transforms)

    output = model(image)[0]  # Extract the output from a batch
    print(output)
    predicted_index = output.argmax(dim=0).item()

    prediction = data_labels[predicted_index]
    return prediction
