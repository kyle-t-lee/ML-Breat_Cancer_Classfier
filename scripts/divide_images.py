# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:53:26 2019

@author: MP_lab_GPU
"""

#!/usr/bin/python3
#coding: utf-8
__author__ = "Fabio Alexandre Spanhol"
__email__ = "faspanhol@gmail.com"

"""

"""
#argv='Normal breast tissue 71138'
#argv2='tubular_adenoma'
#import sys
#import os
#from glob import glob
#import shutil
#
#try:
#     f = open(argv, 'r')
#except IOError:
#    print("Impossible process input file.")
#    sys.exit()
#
#d = {40 :0, 
#     100:0,
#     200:0,
#     400:0}
#
#slides = set() #unordered collection with no duplicat elements
#
##malignant/SOB/ductal_carcinoma/SOB_M_DC-142985/200X : 14
## ./SOB/tubular_adenoma/SOB_B_TA-1415275/200X : 12
##SOB/phyllodes_tumor/SOB_B_PT_14-22704/200X : 42
#
#for row in f:
##    slide = row.split('/')[-2]
#    pic = row.split('/')[-1]
##    k, qt = magnif.split(':')
##    k = int(k.strip()[:-1])
#    	
#    slides.add(slide)
#
#    d[k] += int(qt)
#
#    root="C:\\users\\bcohe\\onedrive\\documents\\Senior Design\\"+str(argv)+str(roow)"
#    for file in os.listdir(root):
#        shutil.move(os.path.join(root, file),'C:\\users\\bcohe\\onedrive\\documents\\Senior Design\\breakhis_v1\\benign_40x')
#
#for k in sorted(d):
#    print(k, d[k])
#
#print('Total slides:%d' % len(slides))  


#%%
import random
import os
import shutil
randomnum=random.uniform(0,1)

root="C:\\Users\\MP_lab_GPU\\Desktop\\\Senior Design 2019\\Cancerous breast tissue"
for file in os.listdir(root):
    randomnum=random.uniform(0,1)
    
    if randomnum<float(0.8):
        shutil.move(os.path.join(root, file),'C:\\Users\\MP_lab_GPU\\Desktop\\\Senior Design 2019\\Senior Design\\breakhis_v1\\train\\malignant')
    else:
        shutil.move(os.path.join(root, file),'C:\\Users\\MP_lab_GPU\\Desktop\\\Senior Design 2019\\Senior Design\\breakhis_v1\\val\\malignant')
        

