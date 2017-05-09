#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue April  19 09:17:02 2017

@author: dhingratul
Tensorflow test program
"""
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
