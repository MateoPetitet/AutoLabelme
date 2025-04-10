'''
Created on Aug 18, 2021

@author: Matéo Petitet for OFB/Parc Naturel Marin de Martinique
'''
# -*- coding: utf-8 -*-
import os
import cv2
import base64
import argparse

parser = argparse.ArgumentParser(description='Generate annotation Labelme JSON files from rectangle cropped images.')
parser.add_argument('--path', type=str, help='Path to the dataset directory')
parser.add_argument('--mode', type=int, choices=[0, 1], default=0,
                    help='Mode: 0 to save in original folders alongside crops, 1 to save in dedicated folder labelme_json')
parser.add_argument('--version', type=str, default='5.2.1',
                    help='Enter labelme version you want to emulate. Default : "5.2.1"')
args = parser.parse_args()

dir_list = os.listdir(args.path)
print(dir_list)

for dossier in dir_list:    # Explore subfolders
    dossier_path = os.path.join(args.path, dossier)
    if os.path.isdir(dossier_path):    # Ensure it's a directory
        files = os.listdir(dossier_path)    # Assume that data structure is folder>subfolder>files
        for image in files:
            image_path = os.path.join(dossier_path, image)
            im = cv2.imread(image_path)
            if im is None:
                continue  # Skip if not an image
            hauteur, largeur, couleur = im.shape
            with open(image_path, "rb") as image_file:
                base64_data = base64.b64encode(image_file.read()).decode("utf-8")
            
            # Determine output directory based on mode
            if args.mode == 0:
                output_dir = dossier_path
            else:
                output_dir = os.path.join(args.path, 'labelme_json')
                os.makedirs(output_dir, exist_ok=True)  # Create directory if missing
            
            # Write JSON file from txt
            txt_filename = image.replace('.PNG', '.txt')
            txt_path = os.path.join(output_dir, txt_filename)
            with open(txt_path, 'w') as f:
                f.write("{\n  \"version\": \""+args.version+"\",\n  \"flags\": {},\n  \"shapes\": [\n    {\n      \"label\": \""+dossier+"\",\n      \"points\": [\n        [\n          0.0,\n          0.0\n        ],\n        [\n          "+str(largeur)+".0,\n          "+str(hauteur)+".0\n        ]\n      ],\n      \"group_id\": null,\n      \"description\": \"\",\n      \"shape_type\": \"rectangle\",\n      \"flags\": {}\n    }\n  ],\n  \"imagePath\": \""+args.path[3:]+"\\\\"+dossier+"\\\\"+image+"\",\n  \"imageData\": \""+base64_data+"\",\n  \"imageHeight\": "+str(hauteur)+",\n  \"imageWidth\": "+str(largeur)+"\n}\n\n")  # Awful but fstrings are not adaptated for our situation
            os.rename(txt_path,txt_path.replace('.txt', '.json'))