from flask import Flask, render_template, request, jsonify
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import tensorflow as tf
import cv2
import nltk
import pickle
import json
import random


app = Flask(__name__)
app.static_folder = 'static'

# Load the trained image classification model
model = load_model('model/deteksi_gigi.h5')
# modelchatBot = load_model('model/model.h5')

# Define classes for image classification
classes = ['Impaksi gigi', 'Implan gigi', 'Kerak Gigi', 'Kista Gigi', 'Odontektomi-Gigi bungsu', 'Endo Primer dengan Periode Sekunder',
           'Lesi Endodontik Primer', 'Lesi Gabungan Sejati', 'Lesi Periodontal Primer', 'Periode Primer dengan Endo Sekunder']

# # Load chatbot-related files
# intents = json.loads(open('data.json').read())
# words = pickle.load(open('model/words.pkl', 'rb'))
# classes_chatbot = pickle.load(open('model/classes.pkl', 'rb'))


# Endpoint for the home page
@app.route('/')
def home():
    return render_template('index.html')


# Endpoint for the image classification page
@app.route('/predict')
def deteksi():
    return render_template('predict.html')


# Endpoint for the about page
@app.route('/about')
def tentang():
    return render_template('about.html')


# Endpoint for processing the uploaded image
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the uploaded image
        img = request.files['file']

        # Convert the image to a NumPy array
        img_array = cv2.imdecode(np.frombuffer(
            img.read(), np.uint8), cv2.IMREAD_COLOR)

        # Resize and preprocess the image
        img_array = cv2.resize(img_array, (224, 224))
        img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0

        # Make prediction
        prediction = model.predict(img_array)

        # Get the predicted class
        predicted_class = classes[np.argmax(prediction)]

        # Get the probability of the predicted class
        probability = "{:.2f}".format(100 * np.max(prediction))

        # Return the result
        return render_template('predict.html', prediction=predicted_class, accuracy=probability)
    except Exception as e:
        # Handle exceptions and provide feedback
        return str(e), 500


# Endpoint for the team page
@app.route('/ourTeam')
def timKami():
    return render_template('OurTeam.html')


# Endpoint for the chatbot page
@app.route('/chatbot')
def chatbot():
    return render_template('Chatbot.html')


if __name__ == '__main__':
    app.run(debug=True)
