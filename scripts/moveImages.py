import random
import os
import shutil

root= r"C:\Users\joekh\Desktop\Senior Design Code\BreaKHis_v1 - Copy copy\malignant\papillary_carcinoma"
for SOB in os.listdir(root):
    SOBpath = os.path.join(root, SOB)
    if(os.path.isdir(SOBpath)):
        for magnif in os.listdir(SOBpath):
            magnifPath = os.path.join(SOBpath, magnif)
            print(magnifPath)
            for file in os.listdir(magnifPath):
                shutil.move(os.path.join(magnifPath, file),root)