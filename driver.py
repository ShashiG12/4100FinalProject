import os
from pathlib import Path
import random
from PIL import Image

"""
File Structure:

This script requires a SOURCE and DESTINATION folder.
NOTE: DESTINATION cannot be in SOURCE.

SOURCE (6 unzipped files of data from https://www.mapillary.com/dataset/places)
└─── 1
└─── 2
└─── 3
└─── 4
└─── 5
└─── 6

DESTINATION (initially empty, but will contain data by cities)
└─── [city 1]
└─── [city 2]
...
└─── [city 30]

"""

# A. SETUP
SOURCE = r'.\Extracted Data'
DESTINATION = r'.\Formatted Data'


# B. HELPERS
# return a list of the directories without any special files
def directories(path):
    return [
        f"{path}/{folder}" for folder in os.listdir(path)
    ]


# make a directory at `DESTINATION/name` if it does not exist
def make_directory(name):
    path = os.path.join(DESTINATION, name)
    try:
        os.mkdir(path)
        print(f"Created folder `{path}`.")
    except FileExistsError:
        print(f"Folder `{path}` already exists.")


# move all non-special files in `src` to `dest`
def move_all(src, dest):
    files = os.listdir(src)

    for file in files:
        if not file.startswith(".") and os.path.isfile(file):
            os.rename(os.path.join(src, file), os.path.join(dest, file))
            #os.rename(f"{src}/{file}", f"{dest}/{file}")


# C. Script
def data_by_city():
    # crawl till the `images` folder
    for folder in directories(SOURCE):
        for subfolder in directories(folder):
            for city_folder in directories(subfolder):
                city_name = Path(city_folder).name

                # 1. make a directory for the city
                make_directory(city_name)

                # 2. find all children image folders
                image_folders = [f"{path}/images" for path in directories(city_folder)]

                # 3. copy all of the images to the destination folder
                for image_folder in image_folders:
                    move_all(image_folder, f"{DESTINATION}/{city_name}")

def openImages():
    for folder in directories(DESTINATION):
        for image in directories(folder):
            try:
                Image.open(image)
            except:
                print(image)


# def directories(path):
#     return [os.path.join(path, folder) for folder in os.listdir(path) if not folder.startswith(".")]

# # Make a directory at `DESTINATION/name` if it does not exist
# def make_directory(name):
#     path = os.path.join(DESTINATION, name)
#     try:
#         os.mkdir(path)
#         print(f"Created folder `{path}`.")
#     except FileExistsError:
#         print(f"Folder `{path}` already exists.")

# # Move all non-special files in `src` to `dest`
# def move_all(src, dest):
#     files = os.listdir(src)
#     for file in files:
#         if not file.startswith("."):
#             os.rename(os.path.join(src, file), os.path.join(dest, file))

# # C. Script
# def data_by_city():
#     # Crawl till the `images` folder
#     for folder in directories(SOURCE):
#         for subfolder in directories(folder):
#             for city_folder in directories(subfolder):
#                 city_name = Path(city_folder).name

#                 # 1. Make a directory for the city
#                 make_directory(city_name)

#                 # 2. Find all children image folders
#                 image_folders = [os.path.join(path,'images') for path in directories(city_folder)]

#                 # 3. Copy all of the images to the destination folder
#                 for image_folder in image_folders:
#                     move_all(image_folder, os.path.join(DESTINATION, city_name))

# # Not needed since TF does this automatically
# def test_train_split():
#     os.mkdir("/Users/rmehta/Desktop/Train")
#     os.mkdir("/Users/rmehta/Desktop/Test")

#     for city_folder in directories(DESTINATION):
#         city_name = Path(city_folder).name
#         images = os.listdir(city_folder)
#         random.shuffle(images)
#         n = len(images)

#         for i, image in enumerate(images):
#             os.rename(
#                 f"{city_folder}/{image}",
#                 f'/Users/rmehta/Desktop/{"Train" if i < n * 0.7 else "Test"}/{city_name}_{image}',
#             )

#         print(f"Moved {n} images from {city_folder}.")


if __name__ == "__main__":
    openImages()
    # test_train_split()
