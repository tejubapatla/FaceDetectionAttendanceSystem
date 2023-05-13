# Face Detection Attendance System

A **Face detection attendance system** is a computer-based system that uses facial recognition technology to mark the attendance of individuals. It works by capturing an image or video of a person's face and comparing it with a database of pre-registered faces to determine the identity of the person.

### Case Study

- *Problem* - 
- *Solution* - 
- *Result* - 

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
1.  Install OpenCV library on your system.
2.  Collect the dataset of faces of people who will be attending the class/meeting.
3.  Train the dataset using a machine learning algorithm like HOG.
4.  Create a Python script that will capture the video feed from a camera.
5.  Use OpenCV to detect faces in the video feed using HOG algorithm.
6.  If a face is detected, compare it with the dataset to check if it matches with any of the faces in the dataset.
7.  If a match is found, mark the attendance for that person.
8.  Save the attendance data in a file or database.
