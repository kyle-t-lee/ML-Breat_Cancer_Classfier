import random
import os
import shutil

root = r"C:\Users\Kyle Lee\Desktop\Senior-Design\ML-Breat_Cancer_Classfier\images\BreaKHis_v1\histology_slides\breast"
#root= r"C:\Users\joekh\Desktop\Senior Design Code\images"
# split root into training, validation, and testing

countTest = 0
countTrain = 0
countVal = 0

for x in os.listdir(root):
    if x == "train" or x== "val" or x=="test":
        #print(x)
        for classification in os.listdir(os.path.join(root,x)):
            classDir = os.path.join(root, x, classification)
            #print(classification)
            for subtype in os.listdir(classDir):
                #print(subtype + ":")
                subclassDir = os.path.join(classDir,subtype)
                #print(subclassDir)
                #print(len(os.listdir(subclassDir)))
                if x == "train":
                    countTrain+=len(os.listdir(subclassDir))
                elif x == "test":
                    countTest+=len(os.listdir(subclassDir))
                else:
                    countVal+=len(os.listdir(subclassDir))
        #print()

total = countTest + countTrain + countVal
print("COUNT TEST: " + str(countTest))
print("COUNT TRAIN: " + str(countTrain))   
print("COUNT VAL: " + str(countVal))
print("COUNT TEST %: " + str(countTest/total))
print("COUNT TRAIN %: " + str(countTrain/total))
print("COUNT VAL %: " + str(countVal/total))

#shutil.move(os.path.join(root, "malignant\\ductol carcinoma\\text.txt"), "C:\\Users\\joekh\\Desktop\\Senior Design Code\\root\\testing\\malignant\\ductol carcinoma")
# for file in os.listdir(root):
#     randomnum=random.uniform(0,1)
    
#     if randomnum<float(0.8):
#         shutil.move(os.path.join(root, file),'C:\\Users\\MP_lab_GPU\\Desktop\\\Senior Design 2019\\Senior Design\\breakhis_v1\\train\\malignant')
#     else:
#         shutil.move(os.path.join(root, file),'C:\\Users\\MP_lab_GPU\\Desktop\\\Senior Design 2019\\Senior Design\\breakhis_v1\\val\\malignant')
