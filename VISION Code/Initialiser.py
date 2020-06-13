import numpy as np
from numpy import sum
import os
import face_recognition
from PIL import Image, ImageDraw
import pickle
import sys
from tkinter.filedialog import askopenfilename

i=0
known_faces=[]
known_face_names=[]
for folders in os.listdir("./pre_img"):
    i=0
    sai_enco_array=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for files in os.listdir("./pre_img/" + folders):
        sai_image = face_recognition.load_image_file("./pre_img/" + folders +"/"+ files)
        sai_face_encoding1 = face_recognition.face_encodings(sai_image)
        if len(sai_face_encoding1) is 1:
        #print(len(sai_face_encoding1))
            sai_enco_array = np.add(sai_face_encoding1[0],sai_enco_array)
            i += 1
    print(np.true_divide(sai_enco_array,i))
    sai_enco_array=np.true_divide(sai_enco_array,i)
    #print((sai_enco_array)/i)
    print(len(sai_enco_array))
    with open("./pre_img/" + folders + "/" + folders + ".txt","wb") as fp:
        pickle.dump(sai_enco_array,fp)
    #known_face_names.append(folders)
#print(known_faces)
#print(known_face_names)
print("Done!!")
