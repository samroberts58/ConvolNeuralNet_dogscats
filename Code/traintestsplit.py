# This code randomly selects 70/30 of the files and places them in train/validation

import os
from random import sample
import pandas as pd
from shutil import copyfile

# Get working directory - 00000 folder
directory = os.getcwd() 

# Within working directory, select random sample
train = []

catlist = pd.Series(os.listdir((directory+'/images/00000')))

n = int(round((len(catlist)*.7),0))

train = catlist.sample(n=n, random_state=0)
catlist.drop(train.index, inplace=True)
# print(listdir)

# Move to train and validation folders
for i in train:
    copyfile("images/00000/" + i, "train/00000/" + i)

for i in catlist:
    copyfile("images/00000/"+ i, "validation/00000/"+ i)
    

# Within working directory, select random sample
train = []

doglist = pd.Series(os.listdir((directory+'/images/00001')))

n = int(round((len(doglist)*.7),0))

train = doglist.sample(n=n, random_state=0)
doglist.drop(train.index, inplace=True)
# print(listdir)

# Move to train and validation folders
for i in train:
    copyfile("images/00001/" + i, "train/00001/" + i)

for i in doglist:
    copyfile("images/00001/"+ i, "validation/00001/" + i)
