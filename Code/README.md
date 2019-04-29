# Is It Raining Cats or Dogs?
# The Code
Leslie Juengst & Samantha Roberts <br/>
Final Project - Group 5


## Retrieve the Data and Organize

1. Go to the following URL and retrieve the images.tar.gz then place in your working directory: 
https://www.kaggle.com/zippyz/cats-and-dogs-breeds-classification-oxford-dataset#images.tar.gz

2. Unzip images.tar.gz in your working directory and an images folder will appear with the jpgs.

3. Make two directories inside the images folder: '00000' and '00001' These will act as class labels.

4. Run renameFiles.py from your working directory.  This should rename and populate the two directory 'labels'.

5. In your working directory, create a 'train' and a 'validation' directory.  Within each of 'train' and 'validation' directories
    create a '00000' and a '00001' directory.  So you should have both 'labels' in 'train' and in 'validation'.

6. Run traintestsplit.py from your working directory.  This will COPY the image files from your images directories into train and validation.
    If you wish to delete the images file following this action, that's your choice.

## Create the lmdb databases from the image files and the mean image

7. Run create_lmdb.py from your working directory.  This will create an oxford_train_lmdb and an oxford_test_lmdb that will be used as
    inputs to the Caffe files.

8. Locate the caffe installation directory and run the following command in your working directory to create the image mean file:
$CAFFE_INSTALLATION/build/tools/compute_image_mean -backend=lmdb oxford_train_lmdb mean.binaryproto

## Caffe Files
Three files are used to run a model in Caffe:
1.  the *_train_test_oxford.prototxt which is the architecture file that defines the network
2.  the *_solver_oxford.prototxt which is the solver file that defines the parameters used for learning
3.  the train_oxford*.py file that is the python file that runs the training and produces graphical outputs

The train_oxford*.py files run caffe on the prototxt files that are contained in this directory. The train_oxford.py code is set
to run either the alexnet files or the lenet files by changing the solver file in line 30 of the python code.  The var1 files all go 
together, and the var2 files go togther.


