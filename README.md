# Is It Raining Cats or Dogs?
Leslie Juengst & Samantha Roberts <br/>
Final Project - Group 5

## Introduction
The ability to properly classify images of different species of animals is a complex and delicate problem. 
The refinement and satisfactory solution to a problem such as this has wide application, such as predictive capabilities for agriculture, health services and animal services. 

This project was designed to classify a variety of cat and dog images according to species. Two convolutional neural networks based on LeNet and AlexNet structures were designed and implemented using Caffe. 



### Data

The data set selected is “Cats and Dogs Breeds Classification Oxford Dataset” on Kaggle.com (dr. Avicenna, 2019).  
<br/> It is comprised of 37 categories of animals, with approximately 200 images per class for a total of 7,393 images.  It was expected that this sizing would provide enough samples for each category to potentially identify unique feature maps for accurate classification purposes. The images themselves are stored as .jpg files, which only required renaming and resizing the images for Caffe.


## Model Design & Instrumentation

### Tools & Software:
```
Python 3.6 was used for image preprocessing efforts.
Python 2.7 was used for training and testing the networks in Caffe.

```

### Files Included:
```
README.md
---
train_oxford.py
train_oxford_var1.py
create_lmdb.py
renameFiles.py
traintestsplit.py
---
alexnet_solver_oxford.prototxt
alexnet_train_text_oxford.prototxt
lenet_solver_oxford.prototxt
lenet_train_test_oxford.prototxt
lenet_solver_oxford_var1.prototxt
lenet_train_test_oxford_var1.prototxt
---
Get_oxford.sh
Create_oxford.sh
---
Images.tar.gz

```

### Process Flow:

Steps for running the project code:

1) Fetch the data from https://www.kaggle.com/zippyz/cats-and-dogs-breeds-classification-oxford-dataset and unzip folders into current working directory.
    *Disregard annotations folder. It was not used for this project.

2) Code to preprocess the data
    * Ensure all filepaths are updated in the code.
    - Run renameFiles.py
    - Remove images with .mat format
    - Separate files by 00/01 and move to folders named '00000' and '00001' to divide classes.
    - Create empty folders named 'train' and 'validation' with two subfolders '00000' and '00001' within each.
    - Run traintestsplit.py 
    - Run create_lmdb.py

3) Code for modeling
    - Run train_oxford.py
        - 1st Run: Ensure line 31 uses 'lenet_solver_oxford.prototxt'
    - Run train_oxford_var1.py
        - Ensure line 31 uses 'lenet_solver_oxford_var1.prototxt'
    - Run train_oxford.py
        - 2nd Run: Update line 31 to use 'alexnet_solver_oxford.prototxt'



## Model Design & Discussion:
```
Metric measurements included: 
    - Accuracy Score
    - Loss value
    - Train/Test time

Overfitting mitigation strategies:
    - Dropout Layers
    - ReLU transfer function
    - Cross-Entropy loss function
    - Softmax output function
    - Minimal layers for less robust data set
```
A preliminary LeNet model was ran to establish a baseline for further comparison. It included two convolutional/pooling layers and two fully connected layers. 

The next model was a LeNet model with updated functions and parameters. It reduced the batch size, increased the number of layers, added dropout layers, and changed the loss function.

The last model was an AlexNet model using the same format and parameters as the LeNet baseline. This model includes 5 convolutional/pooling layers with dropout layers and three fully connected layers.

## Summary

The ideal model was #### with an accuracy score of ##% and a final loss value of ####. It trained in ## seconds and tested in ## seconds. 

One recomendation for future research would be to study the hidden layers' feature maps and attempt to classify images based on subspecies.

