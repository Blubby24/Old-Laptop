# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator

model = tf.keras.models.load_model('models')

img = tf.keras.utils.load_img(
    '28.jpeg', target_size=(150,150,3)
)
img_array = tf.keras.utils.img_to_array(img)
img_array = img_array
img_array = tf.expand_dims(img_array, 0) # Create a batch
img2 = tf.keras.utils.load_img(
    '14.jpeg', target_size=(150,150,3)
)
img2_array =  tf.keras.utils.img_to_array(img2)
img2_array = img2_array
img2_array = tf.expand_dims(img2_array, 0)
imgs = [img_array, img2_array]

predictions = model.predict(img2_array)
predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])
print(score)
print(np.argmax(score))

class_names = ['Jack', 'Nathan']

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)