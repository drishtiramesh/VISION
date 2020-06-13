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
    with open("./pre_img/" + folders +"/" + folders + ".txt","rb") as fp:     
        b=pickle.load(fp)
        known_faces.append(b)
        known_face_names.append(folders)
print(known_faces)
print(known_face_names)

file_name = open("name.txt", "r")
per_name = file_name.read()
print(per_name)

img_path = askopenfilename()
# Load an image with an unknown face
unknown_image = face_recognition.load_image_file(img_path)

# Find all the faces and face encodings in the unknown image
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
# See http://pillow.readthedocs.io/ for more about PIL/Pillow
pil_image = Image.fromarray(unknown_image)
# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.45)

    name = "Unknown"
    print(matches)
    # If a match was found in known_face_encodings, just use the first one.
    if any(matches):
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
    if per_name == "All" or per_name == name:
    # Draw a box around the face using the Pillow module
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw a label with a name below the face
        #myFont = ImageFont.truetype("my-font.ttf", 16)
        text_width, text_height = draw.textsize(name) #, font=myFont)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        draw.text((left + 6, bottom - text_height -5), name, fill=(0, 255, 255, 255))


# Remove the drawing library from memory as per the Pillow docs
del draw

# Display the resulting image
pil_image.show()

# You can also save a copy of the new image to disk if you want by uncommenting this line
# pil_image.save("image_with_boxes.jpg")

