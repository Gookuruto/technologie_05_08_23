import os
import shutil
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import random
import plotly.express as px
import scipy as sp
from keras import Sequential
from keras.src.layers import Dropout, Flatten

from scipy import ndimage
from shutil import copyfile
from tensorflow.keras.layers import Conv2D, Add, MaxPooling2D, Dense, BatchNormalization, Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import LearningRateScheduler
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.layers import MaxPool2D

class_names = ['Cat', 'Dog']

n_dogs = len(os.listdir('./archive/PetImages/Dog'))
n_cats = len(os.listdir('./archive/PetImages/Cat'))
n_images = [n_cats, n_dogs]
plt.pie(n_images, labels=class_names)
# plt.show()

try:
    os.mkdir("tmp")
    os.mkdir('./tmp/cats-v-dogs')
    os.mkdir('./tmp/cats-v-dogs/training')
    os.mkdir('./tmp/cats-v-dogs/validation')
    os.mkdir('./tmp/cats-v-dogs/test')
    os.mkdir('./tmp/cats-v-dogs/training/cats')
    os.mkdir('./tmp/cats-v-dogs/training/dogs')
    os.mkdir('./tmp/cats-v-dogs/validation/cats')
    os.mkdir('./tmp/cats-v-dogs/validation/dogs')
    os.mkdir('./tmp/cats-v-dogs/test/cats')
    os.mkdir('./tmp/cats-v-dogs/test/dogs')
except OSError as e:
    print(e)
    print('Error failed to make directory')

CAT_DIR = './archive/PetImages/Cat'
DOG_DIR = './archive/PetImages/Dog'

TRAINING_DIR = "./tmp/cats-v-dogs/training/"
VALIDATION_DIR = "./tmp/cats-v-dogs/validation/"

TRAINING_CATS = os.path.join(TRAINING_DIR, "cats/")
VALIDATION_CATS = os.path.join(VALIDATION_DIR, "cats/")

TRAINING_DOGS = os.path.join(TRAINING_DIR, "dogs/")
VALIDATION_DOGS = os.path.join(VALIDATION_DIR, "dogs/")

# Define whether to include test split or not
INCLUDE_TEST = True


def split_data(main_dir, training_dir, validation_dir, test_dir=None, include_test_split=True, split_size=0.9):
    """
    Splits the data into train validation and test sets (optional)

    Args:
    main_dir (string):  path containing the images
    training_dir (string):  path to be used for training
    validation_dir (string):  path to be used for validation
    test_dir (string):  path to be used for test
    include_test_split (boolen):  whether to include a test split or not
    split_size (float): size of the dataset to be used for training
    """
    files = []
    for file in os.listdir(main_dir):
        if os.path.getsize(os.path.join(main_dir, file)):  # check if the file's size isn't 0
            files.append(file)  # appends file name to a list

    shuffled_files = random.sample(files, len(files))  # shuffles the data
    split = int(0.9 * len(shuffled_files))  # the training split casted into int for numeric rounding
    train = shuffled_files[:split]  # training split
    split_valid_test = int(split + (len(shuffled_files) - split) / 2)

    if include_test_split:
        validation = shuffled_files[split:split_valid_test]  # validation split
        test = shuffled_files[split_valid_test:]
    else:
        validation = shuffled_files[split:]

    for element in train:
        os.makedirs(os.path.dirname(os.path.join(training_dir, element)), exist_ok=True)
        copyfile(os.path.join(main_dir, element),
                 os.path.join(training_dir, element))  # copy files into training directory

    for element in validation:
        os.makedirs(os.path.dirname(os.path.join(validation_dir, element)), exist_ok=True)
        copyfile(os.path.join(main_dir, element),
                 os.path.join(validation_dir, element))  # copy files into validation directory

    if include_test_split:
        for element in test:
            os.makedirs(os.path.dirname(os.path.join(test_dir, element)), exist_ok=True)
            copyfile(os.path.join(main_dir, element), os.path.join(test_dir, element))  # copy files into test directory
    print("Split sucessful!")


# split_data(CAT_DIR, './tmp/cats-v-dogs/training/cats', './tmp/cats-v-dogs/validation/cats', './tmp/cats-v-dogs/test/cats',INCLUDE_TEST, 0.9)
# split_data(DOG_DIR, './tmp/cats-v-dogs/training/dogs', './tmp/cats-v-dogs/validation/dogs','./tmp/cats-v-dogs/test/dogs',INCLUDE_TEST, 0.9)

train_gen = ImageDataGenerator(
    rescale=1. / 255)

validation_gen = ImageDataGenerator(
    rescale=1. / 255.)

if INCLUDE_TEST:
    test_gen = ImageDataGenerator(
        rescale=1. / 255.)

train_generator = train_gen.flow_from_directory(
    './tmp/cats-v-dogs/training',
    target_size=(224, 224),
    batch_size=64,
    class_mode='binary')
validation_generator = validation_gen.flow_from_directory(
    './tmp/cats-v-dogs/validation',
    target_size=(224, 224),
    batch_size=64,
    class_mode='binary')

if INCLUDE_TEST:
    test_generator = test_gen.flow_from_directory(
        './tmp/cats-v-dogs/validation',
        target_size=(224, 224),
        batch_size=64,
        class_mode='binary')

#### CREATE MODEL

inputs = tf.keras.layers.Input(shape=(150, 150, 3))
x = tf.keras.layers.Conv2D(32, (3, 3), activation='relu')(inputs)
x = tf.keras.layers.Conv2D(64, (3, 3), activation='relu')(x)
x = tf.keras.layers.MaxPooling2D(2, 2)(x)

x = tf.keras.layers.Conv2D(64, (3, 3), activation='relu')(x)
x = tf.keras.layers.Conv2D(128, (3, 3), activation='relu')(x)
x = tf.keras.layers.MaxPooling2D(2, 2)(x)

x = tf.keras.layers.Conv2D(128, (3, 3), activation='relu')(x)
x = tf.keras.layers.Conv2D(256, (3, 3), activation='relu')(x)
x = tf.keras.layers.GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
x = tf.keras.layers.Dense(2, activation='softmax')(x)

model = Sequential([
    Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding = 'same', input_shape=(224,224,3)),
    MaxPool2D(pool_size=(2, 2), strides=2),
    Conv2D(filters=64, kernel_size=(3, 3), activation='relu', padding = 'same'),
    MaxPool2D(pool_size=(2, 2), strides=2),
    Flatten(),
    Dense(units=2, activation='softmax')
])


model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
              loss='sparse_categorical_crossentropy',
              metrics = ['accuracy'])

# model=Sequential()
# model.add(Conv2D(32,(3,3),activation='relu',input_shape=(150, 150, 3)))
# model.add(BatchNormalization())
# model.add(MaxPooling2D(pool_size=(2,2)))
# model.add(Dropout(0.25))
# model.add(Conv2D(64,(3,3),activation='relu'))
# model.add(BatchNormalization())
# model.add(MaxPooling2D(pool_size=(2,2)))
# model.add(Dropout(0.25))
# model.add(Conv2D(128,(3,3),activation='relu'))
# model.add(BatchNormalization())
# model.add(MaxPooling2D(pool_size=(2,2)))
# model.add(Dropout(0.25))
# model.add(Flatten())
# model.add(Dense(512,activation='relu'))
# model.add(BatchNormalization())
# model.add(Dropout(0.5))
# model.add(Dense(1,activation='softmax'))
# model.compile(loss='binary_crossentropy',
#   optimizer='rmsprop',metrics=['accuracy'])

checkpoint_path = "./dog_v_cat_wight/"

cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

#Train

r = model.fit(
         train_generator,
         epochs=10,#Training longer could yield better results
         validation_data=validation_generator)

# tf.keras.saving.save_model(
#     model, './dog_v_cat_wight/model.keras', overwrite=True, save_format=None
# )

# model = tf.keras.saving.load_model("./dog_v_cat_wight/model.keras")
#evalueate


if INCLUDE_TEST:
    model.evaluate(test_generator)



#Visualise

def plot_prediction(generator, n_images):
    """
    Test the model on random predictions
    Args:
    generator: a generator instance
    n_images : number of images to plot

    """
    i = 1
    # Get the images and the labels from the generator
    images, labels = generator.next()
    # Gets the model predictions
    preds = model.predict(images)
    predictions = np.argmax(preds, axis=1)
    labels = labels.astype('int32')
    plt.figure(figsize=(14, 15))
    for image, label in zip(images, labels):
        plt.subplot(4, 3, i)
        plt.imshow(image)
        if predictions[i] == labels[i]:
            title_obj = plt.title(class_names[label])
            plt.setp(title_obj, color='g')
            plt.axis('off')
        else:
            title_obj = plt.title(class_names[label])
            plt.setp(title_obj, color='r')
            plt.axis('off')
        i += 1
        if i == n_images:
            break

    plt.show()

if INCLUDE_TEST:
    plot_prediction(test_generator, 10)
    plot_prediction(validation_generator, 10)