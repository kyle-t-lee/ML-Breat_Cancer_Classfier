import random
import os
import shutil
#randomnum=random.uniform(0,1)

root="C:\\Users\\joekh\\Desktop\\Senior Design Code\\images\\Breakhis"
images = "C:\\Users\\joekh\\Desktop\\Senior Design Code\\images"

# check for testing and validation folders, if not found, create them
testingFolder = False
validationFolder = False
for folders in os.listdir(images):
    if (folders == "testing"):
        testingFolder = True
    if (folders == "validation"):
        validationFolder = True
if (not testingFolder):
    os.mkdir(os.path.join(images,"testing"))
if (not validationFolder):
    os.mkdir(os.path.join(images,"validation"))

# check for malignant and benign folders inside of testing and validation, if not found, create them
malignantFolder = False
benignFolder = False
for classificationFolder in os.listdir(os.path.join(images,"testing")):
    if (classificationFolder == "malignant"):
        malignantFolder = True
    if (classificationFolder == "benign"):
        benignFolder = True
if (not malignantFolder):
    os.mkdir(os.path.join(images,"testing","malignant"))
if (not benignFolder):
    os.mkdir(os.path.join(images,"testing", "benign"))
malignantFolder = False
benignFolder = False
for classificationFolder in os.listdir(os.path.join(images,"validation")):
    if (classificationFolder == "malignant"):
        malignantFolder = True
    if (classificationFolder == "benign"):
        benignFolder = True
if (not malignantFolder):
    os.mkdir(os.path.join(images,"validation","malignant"))
if (not benignFolder):
    os.mkdir(os.path.join(images,"validation", "benign"))

# check for benign subtypes in testing and validation
adenosisFolder=False
fibroadenomaFolder = False
tubularadenomaFolder = False
phyllodesFolder = False
for subtypeFolder in os.listdir(os.path.join(images,"testing","benign")):
    if (subtypeFolder == "adenosis"):
        adenosisFolder=True
    if (subtypeFolder == "fibroadenoma"):
        fibroadenomaFolder=True
    if (subtypeFolder == "tubularadenoma"):
        tubularadenomaFolder = True
    if (subtypeFolder == "phyllodes"):
        phyllodesFolder = True
if (not adenosisFolder):
    os.mkdir(os.path.join(images,"testing", "benign","adenosis"))
if (not fibroadenomaFolder):
    os.mkdir(os.path.join(images,"testing", "benign","fibro adenoma"))
if (not tubularadenomaFolder):
    os.mkdir(os.path.join(images,"testing", "benign", "tubular adenoma"))
if (not phyllodesFolder):
    os.mkdir(os.path.join(images,"testing", "benign", "phyllodes"))
adenosisFolder=False
fibroadenomaFolder = False
tubularadenomaFolder = False
phyllodesFolder = False
for subtypeFolder in os.listdir(os.path.join(images,"validation","benign")):
    if (subtypeFolder == "adenosis"):
        adenosisFolder=True
    if (subtypeFolder == "fibroadenoma"):
        fibroadenomaFolder=True
    if (subtypeFolder == "tubularadenoma"):
        tubularadenomaFolder = True
    if (subtypeFolder == "phyllodes"):
        phyllodesFolder = True
if (not adenosisFolder):
    os.mkdir(os.path.join(images,"validation", "benign","adenosis"))
if (not fibroadenomaFolder):
    os.mkdir(os.path.join(images,"validation", "benign","fibro adenoma"))
if (not tubularadenomaFolder):
    os.mkdir(os.path.join(images,"validation", "benign", "tubular adenoma"))
if (not phyllodesFolder):
    os.mkdir(os.path.join(images,"validation", "benign", "phyllodes"))

# check for malignant subtypes in testing and validation
ductalcarcinomaFolder=False
lobularcarcinomaFolder = False
mucinouscarcinomaFolder = False
papillarycarcinomaFolder = False
for subtypeFolder in os.listdir(os.path.join(images,"testing","malignant")):
    if (subtypeFolder == "ductal carcinoma"):
        ductalcarcinomaFolder=True
    if (subtypeFolder == "lobular carcinoma"):
        lobularcarcinomaFolder=True
    if (subtypeFolder == "mucinous carcinoma"):
        mucinouscarcinomaFolder = True
    if (subtypeFolder == "papillary carcinoma"):
        papillarycarcinomaFolder = True
if (not adenosisFolder):
    os.mkdir(os.path.join(images,"testing", "malignant","ductal carcinoma"))
if (not fibroadenomaFolder):
    os.mkdir(os.path.join(images,"testing", "malignant","lobular carcinoma"))
if (not tubularadenomaFolder):
    os.mkdir(os.path.join(images,"testing", "malignant", "mucinous carcinoma"))
if (not phyllodesFolder):
    os.mkdir(os.path.join(images,"testing", "malignant", "papillary carcinoma"))
ductalcarcinomaFolder=False
lobularcarcinomaFolder = False
mucinouscarcinomaFolder = False
papillarycarcinomaFolder = False
for subtypeFolder in os.listdir(os.path.join(images,"validation","malignant")):
    if (subtypeFolder == "ductal carcinoma"):
        ductalcarcinomaFolder=True
    if (subtypeFolder == "lobular carcinoma"):
        lobularcarcinomaFolder=True
    if (subtypeFolder == "mucinous carcinoma"):
        mucinouscarcinomaFolder = True
    if (subtypeFolder == "papillary carcinoma"):
        papillarycarcinomaFolder = True
if (not adenosisFolder):
    os.mkdir(os.path.join(images,"validation", "malignant","ductal carcinoma"))
if (not fibroadenomaFolder):
    os.mkdir(os.path.join(images,"validation", "malignant","lobular carcinoma"))
if (not tubularadenomaFolder):
    os.mkdir(os.path.join(images,"validation", "malignant", "mucinous carcinoma"))
if (not phyllodesFolder):
    os.mkdir(os.path.join(images,"validation", "malignant", "papillary carcinoma"))


    
# split images into training and validation
for classification in os.listdir(root):
    classDir = os.path.join(root, classification)
    print(classification)
    for subtype in os.listdir(classDir):
        subclassDir = os.path.join(classDir,subtype)
        print(subtype)
        for file in os.listdir(subclassDir):
            randomnum=random.uniform(0,1)
            if randomnum<float(0.5):
                print("Move "+file+" to folder "+ os.path.join(images,"testing",classification,subtype))
                shutil.move(os.path.join(subclassDir, file), os.path.join(images,"testing",classification,subtype))
            else:
                print("Move "+file+" to folder "+ os.path.join(images,"validation",classification,subtype))
                shutil.move(os.path.join(subclassDir, file), os.path.join(images,"validation",classification,subtype))

#shutil.move(os.path.join(root, "malignant\\ductol carcinoma\\text.txt"), "C:\\Users\\joekh\\Desktop\\Senior Design Code\\images\\testing\\malignant\\ductol carcinoma")
# for file in os.listdir(root):
#     randomnum=random.uniform(0,1)
    
#     if randomnum<float(0.8):
#         shutil.move(os.path.join(root, file),'C:\\Users\\MP_lab_GPU\\Desktop\\\Senior Design 2019\\Senior Design\\breakhis_v1\\train\\malignant')
#     else:
#         shutil.move(os.path.join(root, file),'C:\\Users\\MP_lab_GPU\\Desktop\\\Senior Design 2019\\Senior Design\\breakhis_v1\\val\\malignant')
