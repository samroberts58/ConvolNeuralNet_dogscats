# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:55:59 2019

@author: samro
"""

# -*- coding: utf-8 -*-
"""
Machine Learning 2 Project:  Dog/Cat Classification


Data Preprocessing - Rename images and save in different folders based on species.
"""
import os

# Load variable with current working directory to loop through files.
directory = os.getcwd()

dog = 0
cat = 0
for i in os.listdir(directory):  
    if i[0].isupper():
        if cat > 999:
            src = i
            dst = '00-00000-0' + str(cat) + '.jpg'
            os.rename(src, dst)
            cat += 1
        elif cat > 99:
            src = i
            dst = '00-00000-00' + str(cat) + '.jpg'
            os.rename(src, dst)
            cat += 1
        elif cat > 9:
            src = i
            dst = '00-00000-000' + str(cat) + ".jpg"
            os.rename(src, dst)
            cat += 1
        else:
            src = i
            dst = '00-00000-0000' + str(cat) + '.jpg'
            os.rename(src, dst)
            cat += 1
    else:
        if dog > 999:
            src = i
            dst = '01-00000-0' + str(dog) + '.jpg'
            os.rename(src, dst)
            dog += 1 
        elif dog > 99:
            src = i
            dst = '01-00000-00' + str(dog) + '.jpg'
            os.rename(src, dst)
            dog += 1
        elif dog > 9:
            src = i
            dst = '01-00000-000' + str(dog) + ".jpg"
            os.rename(src, dst)
            dog += 1
        else:
            src = i
            dst = '01-00000-0000' + str(dog) + '.jpg'
            os.rename(src, dst)
            dog += 1
    