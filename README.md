# Yolo_Data_Splitter
Python script to create train.txt and test.txt splits from the list of images in yolo-darknet dataset

YOLO (You Only Look Once) neural network based object detection algorithm (originally developed by Joseph Redmon, et. al. https://pjreddie.com/darknet/yolo/ and maintained/improved by Alexey Bochkovskiy, https://github.com/AlexeyAB/darknet ) requires the user to split up their custom training dataset into images used for learning and images used for validating the learning progress during the training. This script allows the user to choose the train/test split percentage and set the location of the dataset.

Repository includes split.py script as well as example train.txt and test.txt files.

Current version is a simple script, where user must copy split.py file into /darknet root directory and run from there. User will be prompted for percentage amount between 10 and 30.

Planned update will have GUI for user to select percentage and image directory.

REQUIRES: 
- Yolo Darknet must be installed, with custom dataset within /darknet/data directory (subdirectories are allowed and will be scanned recursively)
- Python3 must be installed

INSTRUCTIONS:
1) copy split.py into darknet root directory
2) open terminal window within darknet root directory
3) type command: python3 split.py