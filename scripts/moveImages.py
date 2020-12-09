import random
import os
import shutil

#root= r"C:\Users\joekh\Desktop\Senior Design Code\BreaKHis_v1 - Copy copy\malignant\papillary_carcinoma"
#root = r"C:\Users\Kyle Lee\Desktop\Senior-Design\ML-Breat_Cancer_Classfier\images\BreaKHis_v1\histology_slides\breast\malignant\SOB\papillary_carcinoma"
root = r"C:\Users\joekh\OneDrive\Desktop\Senior Design Code\images_V2"
for classification in os.listdir(root): #for benign malig folders
    for subtype in os.listdir(os.path.join(root,classification)):
        for SOBfolder in os.listdir(os.path.join(root,classification,subtype)):
            for magnification in os.listdir(os.path.join(root,classification,subtype, SOBfolder)):
                for file in os.listdir(os.path.join(root,classification,subtype, SOBfolder,magnification)):
                    shutil.move(os.path.join(os.path.join(root,classification,subtype, SOBfolder,magnification), file),os.path.join(root,classification,subtype))