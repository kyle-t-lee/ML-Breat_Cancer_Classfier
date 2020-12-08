#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:26:16 2020

@author: bencohen
"""
import numpy as np
import skimage
import matplotlib.pyplot as plt


#shortcut - change "directory", change file "name"

# Joe's directory
#directory = r"C:\Users\joekh\Documents\GitHub\ML-Breat_Cancer_Classfier\images\contrast_images"

# Kyle's Directory
directory = r"/Users/kylelee/Documents/GitHub/ML-Breat_Cancer_Classfier/images/contrast_images"
os.chdir(directory)
name = 'clear'

if(os.path.exists(name + '.jpeg')):
    image = skimage.color.rgb2gray(skimage.io.imread(directory + "//" + name + '.jpeg'))    # mac/linux directory format
    #image = skimage.color.rgb2gray(skimage.io.imread(directory + "\\" + name + '.jpeg'))   # windows directory format
    y = image[400,:]
    x = np.arange(len(y))

plt.plot(x, y)
plt.xlabel('Pixel')
plt.ylabel('Greyscale Value')
plt.title('Clear')
plt.ylim([0, 1])