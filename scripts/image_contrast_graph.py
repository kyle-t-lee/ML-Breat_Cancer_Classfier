#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:26:16 2020

@author: bencohen
"""
import numpy as np
import skimage
import matplotlib.pyplot as plt



name = 'clear'
image = skimage.color.rgb2gray(skimage.io.imread('/users/bencohen/onedrive/documents/rutgers/senior_design/images/' + name + '.jpeg'))
y = image[400,:]
x = np.arange(len(y))

plt.plot(x, y)
plt.xlabel('Pixel')
plt.ylabel('Greyscale Value')
plt.title('Clear')
plt.ylim([0, 1])