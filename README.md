# Hand Sign Language Entepreter (HaSLI)

<img src="https://user-images.githubusercontent.com/55174887/150554531-dd21514d-cdeb-4809-8835-539c7e691ee3.png" width="200" height="200" />

Lecturer : Prof. Dr. Goh Ong Sing

Project Manager: Ahmad Syazani Aniq bin Ahmad Khaizi
Project Members: 
  1) Hasif bin Mohamad Noh
  2) Muhammad Naqib Hakimi bin Hakmal
  3) Aiman Faris b. Mazri

Download the [APK File](https://drive.google.com/file/d/1VqzHEgbA8BqpSgVJruktaNIwynxj16w1/view?usp=sharing)

## Introduction

  HaSLI is a mobile app that can translate hand sign language into alphabet by using real-time camera. HaSLI can help people to interact with mute or deaf people or they can use this app to learn the sign language

  This app also provided all the sign language alphabets. User can practice using this app.
  
## Objectives

1) To help people understand the sign language
2) To help people to communicate with mute or deaf people
3) To help people learn and practice this language

## Design & Model

There are 2 layers of AI implemented in this project:
  1. [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html) (Library to tracks hand)
  2. Neural Network (To trace the hand signs)\n
    - Layer 1 / Input Layer (150 Nodes, Sigmoid Activation Function)\n
    - Layer 2 / Hidden Layer (150 Nodes, Sigmoid Activation Function)\n
    - Layer 3 / Output Layer (26 Nodes)\n

## Data

Data were gathered manually 

## Screenshots

![Picture1](https://user-images.githubusercontent.com/55174887/150564341-4127e955-76dd-48c4-9fa3-8edddfc5e4e4.jpg)
![Picture2](https://user-images.githubusercontent.com/55174887/150564347-40007410-8e8a-4114-9fb7-2bd733d21651.jpg)
![Picture3](https://user-images.githubusercontent.com/55174887/150564353-2ec0953b-2e8c-4145-ba29-54ab0cda0d8f.jpg)
