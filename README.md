# AiFi
AiFi Project-Tensorflow

Here is the written exercise as we discussed. You have three days to work on it. Enjoy the journey of learning and exploring!

Convolutional neural networks have been very successful in the field of computer vision. The network is typically large, very deep, and is composed of multiple layers of neurons with millions of parameters. Despite impressive results in accuracy, models are often too large to be deployed on devices with limited resources e.g. mobile phones and IoT devices.

In this challenge, you will be our superhero in shrinking the network size to its absolute minimum. You are right. Less is more! First, take a look at this TensorFlow tutorial on MNIST: https://www.tensorflow.org/get_started/mnist/pros

We suggest you go through the tutorial and understand the basics of how to use TensorFlow for training and debugging. Once you feel comfortable about training your own mini DNN on MNIST. Read the following questions:

Q1: How many parameters does your initial model contain? What is the memory footprint? What is the accuracy on the testing data set?

Q2: Design experiments on how we can trade accuracy with model size. Let's say your initial model accuracy is 98%. What would be the minimum model size if we are willing to reduce the accuracy to no less than 95%. Explain your design choice. 

Q3: Let s(f) be the minimum model size that can achieve accuracy f. 

Given 0 <= f_1 < f_2 < ... < f_n  < =1, do you agree that:

0 < s(f_1) < s(f_2) < ... < s(f_n) 

Can you prove / disprove the above conjecture in your design space? If you cannot justify it mathematically, experimental plots would qualify as well.

Write a report to share your findings.


Bonus: Instead of MNIST, you can repeat your experiment on CIFAR or even ImageNet if you have many GPUs at hand. This is not required but could be tons of fun.

Thanks again for taking the time, and I look forward to keeping in touch.

Best,
Liu 
 
AD
