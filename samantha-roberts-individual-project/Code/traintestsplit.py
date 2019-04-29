# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 21:04:06 2019

@author: samro
"""

import os
from random import sample
import pandas as pd

# Get working directory - 00000 folder
directory = os.getcwd() 

# Within working directory, select random sample
train = []

listdir = pd.Series(os.listdir(directory))

n = int(round((len(listdir)*.7),0))

train = listdir.sample(n=n, random_state=0)
listdir.drop(train.index, inplace=True)
# print(listdir)

# Move to train and validation folders
for i in train:
    os.rename("C:\\Users\\samro\\Desktop\\GW\\Mach Learn 2\\Deep-Learning\\Caffe_\\FinalProject\\00000" + "\\"+ i, "C:\\Users\\samro\\Desktop\\GW\\Mach Learn 2\\Deep-Learning\\Caffe_\\FinalProject\\train\\00000"+"\\"+i)

for i in listdir:
    os.rename("C:\\Users\\samro\\Desktop\\GW\\Mach Learn 2\\Deep-Learning\\Caffe_\\FinalProject\\00000\\"+ "\\"+ i, "C:\\Users\\samro\\Desktop\\GW\\Mach Learn 2\\Deep-Learning\\Caffe_\\FinalProject\\validation\\00000\\"+ "\\"+ i)
    


# Repeat for dogs - change working directory to 00001 folder
directory = os.getcwd() 

# Within working directory, select random sample
train = []

listdir = pd.Series(os.listdir(directory))

n = int(round((len(listdir)*.7),0))

train = listdir.sample(n=n, random_state=0)
listdir.drop(train.index, inplace=True)
# print(listdir)

# Move to train and validation folders
for i in train:
    os.rename("C:\\Users\\samro\\Desktop\\GW\\Mach Learn 2\\Deep-Learning\\Caffe_\\FinalProject\\00001" + "\\"+ i, "C:\\Users\\samro\\Desktop\\GW\\Mach Learn 2\\Deep-Learning\\Caffe_\\FinalProject\\train\\00001"+"\\"+i)

for i in listdir:
    os.rename("C:\\Users\\samro\\Desktop\\GW\\Mach Learn 2\\Deep-Learning\\Caffe_\\FinalProject\\00001\\"+ "\\"+ i, "C:\\Users\\samro\\Desktop\\GW\\Mach Learn 2\\Deep-Learning\\Caffe_\\FinalProject\\validation\\00001\\"+ "\\"+ i)
    
