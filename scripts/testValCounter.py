import random
import os
import shutil

root= r"C:\Users\joekh\Desktop\Senior Design Code\images"
# split root into training and validation
countTest = 0
countVal = 0
for x in os.listdir(root):
    if x == "test" or x== "val":
        print(x)
        for classification in os.listdir(os.path.join(root,x)):
            classDir = os.path.join(root, x, classification)
            print(classification)
            for subtype in os.listdir(classDir):
                print(subtype + ":")
                subclassDir = os.path.join(classDir,subtype)
                print(len(os.listdir(subclassDir)))
        print()
            

#shutil.move(os.path.join(root, "malignant\\ductol carcinoma\\text.txt"), "C:\\Users\\joekh\\Desktop\\Senior Design Code\\root\\testing\\malignant\\ductol carcinoma")
# for file in os.listdir(root):
#     randomnum=random.uniform(0,1)
    
#     if randomnum<float(0.8):
#         shutil.move(os.path.join(root, file),'C:\\Users\\MP_lab_GPU\\Desktop\\\Senior Design 2019\\Senior Design\\breakhis_v1\\train\\malignant')
#     else:
#         shutil.move(os.path.join(root, file),'C:\\Users\\MP_lab_GPU\\Desktop\\\Senior Design 2019\\Senior Design\\breakhis_v1\\val\\malignant')
