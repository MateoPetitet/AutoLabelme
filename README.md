# Auto Labelme

This script aims to automaticaly create labelme-like labels from cropped rectangular images, replicating json structure from [labelme](https://github.com/wkentaro/labelme) 5.2.1. This is useful in case someone extracted regions of interest corresponding to one label from pictures without using dedicated labeling tools.

## Data structure
Data is expected to follow this structure : 
```bash
├─── data_folder
│   ├─── label_1
│   │   ├─── file_1_1.png
│   │   ├─── file_1_2.png
│   │   ├─── file_1_3.png
│   ├─── label_2
│   │   ├─── file_2_1.png
│   │   ├─── file_2_2.png
│   │   ├─── file_2_3.png
│   ├─── label_3
│   │   ├─── file_3_1.png
│   │   ├─── file_3_2.png
│   │   ├─── file_3_3.png
```
The <kbd>.json</kbd> files created will be named like the file they describe, using the label from the folder containing it.

## Parameters Explained

**- -path** Path to the dataset directory
**- -mode (optional)** Value : 0 or 1, default to 0. Save <kbd>.json</kbd> files in the same folder as their corresponding pictures (0) or in a dedicated folder <kbd>labels_json</kbd> (1). The latter was specifically added to use [Labelme2YOLO](https://github.com/rooneysh/Labelme2YOLO).
**- -version (optional)** Specify the labelme version you want to write in the <kbd>.json</kbd> files. Defaults to "5.2.1".

## How to Use

### 1. Convert crops to .json
Put crops in folders named like their labels then run :
```bash
python auto_labelme.py --path "C:/data_folder"
```
The output will look like this :
```bash
├─── data_folder
│   ├─── label_1
│   │   ├─── file_1_1.png
│   │   ├─── file_1_2.png
│   │   ├─── file_1_3.png
│   │   ├─── file_1_1.json
│   │   ├─── file_1_2.json
│   │   ├─── file_1_3.json
│   ├─── label_2
│   │   ├─── file_2_1.png
│   │   ├─── file_2_2.png
│   │   ├─── file_2_3.png
│   │   ├─── file_2_1.json
│   │   ├─── file_2_2.json
│   │   ├─── file_2_3.json
│   ├─── label_3
│   │   ├─── file_3_1.png
│   │   ├─── file_3_2.png
│   │   ├─── file_3_3.png
│   │   ├─── file_3_1.json
│   │   ├─── file_3_2.json
│   │   ├─── file_3_3.json
```

### 2. Convert crops to .json and put them in a new folder (use for [Labelme2YOLO](https://github.com/rooneysh/Labelme2YOLO))

Put crops in folders named like their labels then run :
```bash
python auto_labelme.py --path "C:/data_folder" --mode 1
```
The output will look like this :
```bash
├─── data_folder
│   ├─── label_1
│   │   ├─── file_1_1.png
│   │   ├─── file_1_2.png
│   │   ├─── file_1_3.png
│   ├─── label_2
│   │   ├─── file_2_1.png
│   │   ├─── file_2_2.png
│   │   ├─── file_2_3.png
│   ├─── label_3
│   │   ├─── file_3_1.png
│   │   ├─── file_3_2.png
│   │   ├─── file_3_3.png
│   ├─── labelme_json
│   │   ├─── file_1_1.json
│   │   ├─── file_1_2.json
│   │   ├─── file_1_3.json
│   │   ├─── file_2_1.json
│   │   ├─── file_2_2.json
│   │   ├─── file_2_3.json
│   │   ├─── file_3_1.json
│   │   ├─── file_3_2.json
│   │   ├─── file_3_3.json
```