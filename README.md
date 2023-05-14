# Face Detection Attendance System

A **Face detection attendance system** is a computer-based system that uses facial recognition technology to mark the attendance of individuals. It works by capturing an image or video of a person's face and comparing it with a database of pre-registered faces to determine the identity of the person.

### Case Study

- *Problem* - Taking attendanace manually by wasting time for every class throughout the day.
- *Solution* - Digitalizing this process to save time and maintain records of data which can be used later.
- *Result* - Lot of time can be saved and can use and maintain this data much more efficiently.

**Techonolgies used :**

-   Programming language : Python
-   Database : Microsoft Access
-   Python Library : Open CV, numpy,pandas, matplotlib (these are the main ones. we have used many other for internal calculations)
-   Algorithm : HOG

## Decoding the Algorithm

### What is OpenCV?
OpenCV is a popular open-source computer vision library that can be used to perform face detection. It has more than 2,500 optimized algorithms, which includes a comprehensive set of both classic and state-of-the-art computer vision and machine learning algorithms. There are a variey of algorithms used for face recognition like :
- Haar Cascades
- Local Binary Patterns (LBP)
- Convolutional Neural Networks (CNN)
- Histogram of Oriented Gradients (HOG)

Each algorithm has its own strengths and weaknesses, and the choice of algorithm depends on the specific requirements of the application.

### What is HOG algorithm?
HOG stands for Histogram of oriented gradients. HOG is a popular feature descriptor used for object detection. It works by dividing the image into small cells and calculating the gradient orientation and magnitude in each cell. These values are then used to create a histogram of oriented gradients, which is used to train a machine learning algorithm to detect objects in the image.

Below is the flow of how HOG algorithm works:
![Block diagram](https://github.com/Teju-tech/FaceDetectionAttendanceSystem/assets/60033684/80634d95-15cf-4ed9-b607-ab4d14bfd06f)

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

**Note** :

- I made this attendance system as a mobile app based on our requirements. You can implement this as a dedicated web app or integrate this into your college/Organization website as well.
- Not included all the files we used in this project. Sharing just the heart of the system. rest al can be build based on the requirements and usage.
