import random
import os
import shutil
#randomnum=random.uniform(0,1)

root= r"C:\Users\joekh\Desktop\Senior Design Code\images"

# check for testing and validation folders, if not found, create them
if (not os.path.isdir(os.path.join(root,"test"))):
    os.mkdir(os.path.join(root,"test"))
if (not os.path.isdir(os.path.join(root,"val"))):
    os.mkdir(os.path.join(root,"val"))

# check for malignant and benign folders inside of testing and validation, if not found, create them
if (not os.path.isdir(os.path.join(root,"test","malignant"))):
    os.mkdir(os.path.join(root,"test","malignant"))
if (not os.path.isdir(os.path.join(root,"test","benign"))):
    os.mkdir(os.path.join(root,"test", "benign"))

if (not os.path.isdir(os.path.join(root,"val","malignant"))):
    os.mkdir(os.path.join(root,"val","malignant"))
if (not os.path.isdir(os.path.join(root,"val","benign"))):
    os.mkdir(os.path.join(root,"val", "benign"))

# check for test malignant subtypes
if (not os.path.isdir(os.path.join(root,"test","malignant","ductal_carcinoma"))):
    os.mkdir(os.path.join(root,"test","malignant","ductal_carcinoma"))
if (not os.path.isdir(os.path.join(root,"test","malignant","lobular_carcinoma"))):
    os.mkdir(os.path.join(root,"test","malignant","lobular_carcinoma"))
if (not os.path.isdir(os.path.join(root,"test","malignant","mucinous_carcinoma"))):
    os.mkdir(os.path.join(root,"test","malignant","mucinous_carcinoma"))
if (not os.path.isdir(os.path.join(root,"test","malignant","papillary_carcinoma"))):
    os.mkdir(os.path.join(root,"test","malignant","papillary_carcinoma"))

# check for val malignant subtypes
if (not os.path.isdir(os.path.join(root,"val","malignant","ductal_carcinoma"))):
    os.mkdir(os.path.join(root,"val","malignant","ductal_carcinoma"))
if (not os.path.isdir(os.path.join(root,"val","malignant","lobular_carcinoma"))):
    os.mkdir(os.path.join(root,"val","malignant","lobular_carcinoma"))
if (not os.path.isdir(os.path.join(root,"val","malignant","mucinous_carcinoma"))):
    os.mkdir(os.path.join(root,"val","malignant","mucinous_carcinoma"))
if (not os.path.isdir(os.path.join(root,"val","malignant","papillary_carcinoma"))):
    os.mkdir(os.path.join(root,"val","malignant","papillary_carcinoma"))

# check for test benign subtypes
if (not os.path.isdir(os.path.join(root,"test","benign","adenosis"))):
    os.mkdir(os.path.join(root,"test", "benign","adenosis"))
if (not os.path.isdir(os.path.join(root,"test","benign","fibroadenoma"))):
    os.mkdir(os.path.join(root,"test", "benign","fibroadenoma"))
if (not os.path.isdir(os.path.join(root,"test","benign","phyllodes_tumor"))):
    os.mkdir(os.path.join(root,"test", "benign","phyllodes_tumor"))
if (not os.path.isdir(os.path.join(root,"test","benign","tubular_adenoma"))):
    os.mkdir(os.path.join(root,"test", "benign","tubular_adenoma"))

# check for val benign subtypes
if (not os.path.isdir(os.path.join(root,"val","benign","adenosis"))):
    os.mkdir(os.path.join(root,"val", "benign","adenosis"))
if (not os.path.isdir(os.path.join(root,"val","benign","fibroadenoma"))):
    os.mkdir(os.path.join(root,"val", "benign","fibroadenoma"))
if (not os.path.isdir(os.path.join(root,"val","benign","phyllodes_tumor"))):
    os.mkdir(os.path.join(root,"val", "benign","phyllodes_tumor"))
if (not os.path.isdir(os.path.join(root,"val","benign","tubular_adenoma"))):
    os.mkdir(os.path.join(root,"val", "benign","tubular_adenoma"))



    
# split root into training and validation
# creates a new folder called test and val with benign malig and sub types
for classification in os.listdir(root):
    if classification == "benign" or classification == "malignant":
        classDir = os.path.join(root, classification)
        print(classification)
        for subtype in os.listdir(classDir):
            subclassDir = os.path.join(classDir,subtype)
            print(subtype)
            for file in os.listdir(subclassDir):
                randomnum=random.uniform(0,1)
                if randomnum<float(0.7):
                    print("Copy "+file+" to folder "+ os.path.join(root,"test",classification,subtype))
                    shutil.copy(os.path.join(subclassDir, file), os.path.join(root,"test",classification,subtype))
                else:
                    print("Copy "+file+" to folder "+ os.path.join(root,"val",classification,subtype))
                    shutil.copy(os.path.join(subclassDir, file), os.path.join(root,"val",classification,subtype))

#shutil.move(os.path.join(root, "malignant\\ductol carcinoma\\text.txt"), "C:\\Users\\joekh\\Desktop\\Senior Design Code\\root\\testing\\malignant\\ductol carcinoma")
# for file in os.listdir(root):
#     randomnum=random.uniform(0,1)
    
#     if randomnum<float(0.8):
#         shutil.move(os.path.join(root, file),'C:\\Users\\MP_lab_GPU\\Desktop\\\Senior Design 2019\\Senior Design\\breakhis_v1\\train\\malignant')
#     else:
#         shutil.move(os.path.join(root, file),'C:\\Users\\MP_lab_GPU\\Desktop\\\Senior Design 2019\\Senior Design\\breakhis_v1\\val\\malignant')
