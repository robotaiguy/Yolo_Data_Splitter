
from pathlib import Path

# set path where images are stored, relative to split.py location
#img_path = ".darknet/data"
img_path = "/home/skynet/darknet/data"

# display image path on screen
print("Image directory: " + img_path)

# percentage of images to be used for the test set
pcnt_test = 10;

# create and/or truncate train.txt and test.txt
file_train = open("train.txt", "w")
file_test = open("test.txt", "w")

# populate train.txt and test.txt
counter = 1
index_test = round(100 / pcnt_test)

for path in Path(img_path).rglob("*.jpg"):

    if counter == index_test:
        counter = 1
        file_test.write(str(path) + "\n")
    else:
        file_train.write(str(path) + "\n")
        counter += 1;
