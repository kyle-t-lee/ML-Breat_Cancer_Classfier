# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:40:39 2019

@author: MP_lab_GPU
"""

from __future__ import print_function, division

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import copy
from PIL import Image


#repo_dir = 'C:\\Users\MP_lab_GPU\Desktop\Senior Design 2019\Senior Design\'
repo_dir = '/Users/bencohen/OneDrive/Documents/Rutgers/repo/'
#%%
imsize = 256
loader = transforms.Compose([
            transforms.RandomSizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

#
def image_loader(loader, image_name):
    image = Image.open(image_name)
    image = loader(image).float()
    image = torch.tensor(image, requires_grad=True)
    image = image.unsqueeze(0)
    return image

model = models.resnet152(pretrained=True)
num_ftrs = model.fc.in_features

model.fc = nn.Linear(num_ftrs, 2)
model.load_state_dict(torch.load(repo_dir + '/model/model_state_dict_combined.pt', map_location=torch.device('cpu')))
model.eval()
malignant_path = repo_dir + '/images/cropped_test/Malignant/'
non_malignant_path = repo_dir + '/images/cropped_test/Non-Malignant/'
#%%
#### THE FIRST ARGUMENT IS BENIGN, SECOND IS MALIGNANT
tp = [] #num correctly diagnosed malignant
fp = [] #num incorrectly diagnosed malignant
tn = [] #num correctly diagnosed benign
fn = [] #num incorrectly diagnosed negative
errors = 0
num_malignant = 0
num_non_malignant = 0

for i in os.listdir(malignant_path):
    try:
        image = image_loader(loader, os.path.join(malignant_path, i))
        
        y = model(image)
        if y.argmax().item() == 0:
            fn.append(i)
        else:
            tp.append(i)
        num_malignant +=1
    except:
        print(i)
        errors +=1
        
for i in os.listdir(non_malignant_path):
    try:
        image = image_loader(loader, os.path.join(non_malignant_path, i))
        num_non_malignant +=1
        y = model(image)
        if y.argmax().item() == 0:
            tn.append(i)
        else:
            fp.append(i)
    except:
        errors +=1

    
            
    
    
#%%







