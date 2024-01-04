print("Activated")
import tensorflow as tf
import os
from PIL import Image

print("Activated")

def recognize(path):

    # Define the threshold value.
    threshold = 0.5

    # Load the model.
    model = tf.keras.models.load_model('resnet50.h5')
    l = os.listdir(r"Vegetable Images\test")

    # Preprocess the image.
    image = tf.keras.preprocessing.image.load_img(path, target_size=(224, 224))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.expand_dims(image, axis=0)

    # Make a prediction.
    prediction = model.predict(image)
    class_labels_list = list(prediction)

    predictions_above_threshold = []

    for i in range(len(class_labels_list[0])):
        if class_labels_list[0][i]>=threshold:
            # print(l[i])
            predictions_above_threshold.append(l[i])

    return predictions_above_threshold