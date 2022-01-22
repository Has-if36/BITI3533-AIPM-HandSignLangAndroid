# Hand Sign Language Entepreter (HaSLI)

## A. DEFINING THE PROJECT

Developed by Ad Astra Sdn. Bhd.
<img src="https://user-images.githubusercontent.com/55174887/150628368-dc441e3d-01f0-4a7d-ab44-db3d2212d9be.png" width="200" height="200" />

Lecturer : Prof. Dr. Goh Ong Sing

Project Manager: Ahmad Syazani Aniq bin Ahmad Khaizi
Project Members: 
  1) Hasif bin Mohamad Noh
  2) Muhammad Naqib Hakimi bin Hakmal
  3) Aiman Faris b. Mazri

Download the [APK File](https://drive.google.com/file/d/1VqzHEgbA8BqpSgVJruktaNIwynxj16w1/view?usp=sharing)

### Introduction

  HaSLI is a mobile app that can translate hand sign language into alphabet by using real-time camera. HaSLI can help people to interact with mute or deaf people or they can use this app to learn the sign language

  This app also provided all the sign language alphabets. User can practice using this app.
  
### Objectives

1) To help people understand the sign language
2) To help people to communicate with mute or deaf people
3) To help people learn and practice this language

## B. PLANNING THE PROJECT
## C. IMPLEMENTING THE PROJECT PLAN
## D. EXECUTING THE PROJECT
### Design & Model

<p align="center">
  <img width="598" height="151" src="./image/model.png">
  <br>
  <em>Figure D.1: Overview of the Model</em>
</p>

Figure D.1 shows how the system works. There are 2 layers of AI implemented in this project:
  1. [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html) (Library to tracks hand)
  2. Neural Network (To trace the hand signs)
    <p align="center">
    <img width="394" height="394" src="./image/NeuralNet.png">
    <br>
    <em>Figure D.2: Neural Network</em>
    </p>
    Figure D.2 Shows the design for the Neural Network:
      1. Layer 1 / Input Layer (150 Nodes, Sigmoid Activation Function)
      2. Layer 2 / Hidden Layer (150 Nodes, Sigmoid Activation Function)
      3. Layer 3 / Output Layer (26 Nodes)
    


### Data

Data were gathered manually. The data gathering was improvised and updated up until Version 4. HandRecBaseV4.py was used to gather the data. The gathered data was trained using hand_sign_nn.ipynb and then tested using HandRecBaseV4Test.py.

<p align="center">
  <img width="1000" height="387" src="./image/sample_data.png">
  <br>
  <em>Figure D.3: Sample Data Gathered for Training Model</em>
</p>

Figure D.3 shows the sample of the training data. Iniside this data, there are total of 150 (25x6) features inside the data. These features are divided into 6 sections. This is to make the system to have a capability to capture hand sign which has motion. The 25 [0-24] feature in each section are the distance of 2 Points from the hand tracking.

<p align="center">
  <img width="476" height="511" src="./image/HandRecBaseV2_ref.png">
  <br>
  <em>Figure D.4: Reference for the Feature</em>
</p>

Figure D.4 shows the reference for the feature where from 0 to 24 are the distances of 2 Points as mentioned. Each section has a delay of 0.25 seconds. This means that, for the gathering data, the program will read the data every 0.25 seconds, for 6 times. Thus, the system should be able to capture hand sign that has motion of up to 1.5 seconds.

### Comparing with CNN Model
As far as we understand,
#### Pros over CNN
  - Simple, meaning it can run faster
  - It capable of capturing hand sign with motion like alphabet J and Z

#### Cons over CNN
  - Less Accurate
  - It will continuously reads the hand sign even though the user does not have the intention to make a hand sign

### Coding

<p align="center">
  <img width="564" height="500" src="./image/data_code.png">
  <br>
  <em>Figure D.5: Codes for the Data Gathering</em>
</p>

Figure D.5 shows the codes for the data gathering. In this part of code, the program will capture the 25 distances every 0.25 seconds. When the program has scanned for 6 times, it will stop collecting the data and ready to collect for the next data.

<p align="center">
  <img width="564" height="500" src="./image/data_code.png">
  <br>
  <em>Figure D.5: Codes for Mobile Development</em>
</p>

### Project Result

![Picture1](https://user-images.githubusercontent.com/55174887/150564341-4127e955-76dd-48c4-9fa3-8edddfc5e4e4.jpg)
![Picture2](https://user-images.githubusercontent.com/55174887/150564347-40007410-8e8a-4114-9fb7-2bd733d21651.jpg)
![Picture3](https://user-images.githubusercontent.com/55174887/150564353-2ec0953b-2e8c-4145-ba29-54ab0cda0d8f.jpg)\
<img src="./image/result_1.png" alt="Result" width="205"/>
<img src="./image/result_2.png" alt="Interface" width="205"/>
<p align="center">
  <img width="191" height="408" src="https://user-images.githubusercontent.com/55174887/150564341-4127e955-76dd-48c4-9fa3-8edddfc5e4e4.jpg">
  <img width="191" height="408" src="https://user-images.githubusercontent.com/55174887/150564347-40007410-8e8a-4114-9fb7-2bd733d21651.jpg">
  <img width="191" height="408" src="https://user-images.githubusercontent.com/55174887/150564353-2ec0953b-2e8c-4145-ba29-54ab0cda0d8f.jpg">
  <br>
  <img width="205" height="408" src="./image/result_1.png">
  <img width="205" height="408" src="./image/result_2.png">
  <br>
  <em>Figure D.6: Result of the Project</em>
</p>

Figure D.6 shows the output from the project. On the bottom right image, they are the interfaces for:
1. Spaces for Character to build into word
2. Letter that was recognised
3. Button to add space into (1)
4. Button to take the character recognised from (2) into (1)
5. Button to clear up (1)
6. Button to switch the camera
7. Frame rate
8. Button to go to Hand Sign List

## E. COMPLETING THE PROJECT

## F PROJECT PRESENTATION
[![https://www.youtube.com/watch?v=ALqI2aP-8_c](https://res.cloudinary.com/marcomontalbano/image/upload/v1642827633/video_to_markdown/images/youtube--ALqI2aP-8_c-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/ALqI2aP-8_c "https://www.youtube.com/watch?v=ALqI2aP-8_c")
