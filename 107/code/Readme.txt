Development Environment details :

Machine: Windows 10 
Python 3.6.2 :: Anaconda custom (64-bit)

Test Environment details : 
Machine : Ubuntu 16.04 LTS

Docker installed on Ubuntu (Linux) machine 
To install docker use the follwing command
sudo apt install docker.io 

This folder contains the following files: 

Dockerfile : to build the image for running the program in a container.

Commads to build the image from inside the code folder

docker build -t image_tag .

docker run --name container_name image_name

minimalNetwork.py : solution to the Problem Euler Problem 107

test_minimalNetwork.py : unit test cases written to the test the miminalNetwork module

test_input.txt : sample test case for testing the code.

p107_network.txt : the test case provided by the project euler to test the solution

 
To run the test cases :

run the follwing command from the code folder

pytest
