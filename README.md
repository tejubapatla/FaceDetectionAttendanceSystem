# Face Detection Attendance System

A **Face detection attendance system** is a computer-based system that uses facial recognition technology to mark the attendance of individuals. It works by capturing an image or video of a person's face and comparing it with a database of pre-registered faces to determine the identity of the person.

### Case Study

- *Problem* - Taking attendanace manually by wasting time for every class throughout the day.
- *Solution* - Digitalizing this process to save time and maintain records of data which can be used later.
- *Result* - Lot of time can be saved and can use and maintain this data much more efficiently.

**Techonolgies used :**

-   Programming language : Python
-   Database : Microsoft Access
-   Python Library : Open CV
-   Algorithm : HOG

## Decoding the Algorithm

### What is OpenCV?
OpenCV is a popular open-source computer vision library that can be used to perform face detection. It provides pre-trained models for face detection that can be used to quickly build a face detection system. OpenCV also provides tools for image processing, such as resizing and filtering, which can be used to improve the accuracy of the face detection system.

### What is HOG algorithm?

HOG stands for Histogram of oriented gradients. HOG is a popular feature descriptor used for object detection. It works by dividing the image into small cells and calculating the gradient orientation and magnitude in each cell. These values are then used to create a histogram of oriented gradients, which is used to train a machine learning algorithm to detect objects in the image.

## What Steps I followed to design this system?

Steps involved in designing this app :
1.  Installed OpenCV library.
2.  Collected the dataset of my classmates faces to train.
3.  Trained the dataset using a machine learning algorithm called HOG (Histogram of oriented gradients).
4.  Created a Python script that will recognize the faces from the picture that is given as input to this script.
5.  Face Recognition part will be taken care by OpenCV using HOG algorithm.
6.  If the face is detected, then the algorithm compares it with the dataset to check if it matches with any of the faces in the dataset.
7.  If the match is found, Python script marks the attendance for that person in a excel sheet.
8.  This excel sheet can be stored in a database or used for any reporting purposes.

**Note** - I made this attendance system as a mobile app based on our requirements. You can implement this as a dedicated web app or integrate this into your college/Organization website as well.
