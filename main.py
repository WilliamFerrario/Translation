import os
from flask import Flask, render_template, request
from google.cloud import translate_v2 as translate

app = Flask(__name__)

# Set the path to the JSON key file manually
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/DubsF/AppData/Roaming/gcloud/application_default_credentials.json'

# Initialize a Translate client object
client = translate.Client()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    # Get the text to be translated from the form data
    text = request.form['text']

    # Translate the text using the Google Cloud Translation API
    translation = client.translate(text, target_language='en')

    # Return the translated text
    return render_template('index.html', translation=translation['translatedText'])

if __name__ == '__main__':
    app.run(debug=True)