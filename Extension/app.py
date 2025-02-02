from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from flask_cors import CORS
import dill as pickle


app = Flask(__name__)
CORS(app)

with open('best_model_hoi (4).pkl', 'rb') as f:
    model = pickle.load(f)

with open('best_vectorizer_hoi (4).pkl', 'rb') as f:
    vectorizer = pickle.load(f)




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # text = request.form.get('text')
    data = request.get_json()  # Get JSON input
    text = data.get('text') 
    if text is not None:
        text_transformed = vectorizer.transform([text])

        prediction = model.predict(text_transformed)

        return jsonify({'prediction': int(prediction[0])})
    else:
        return jsonify({'error': 'Input text not provided.'})

if __name__ == '__main__':
    app.run(debug=True)
    # with open('best_model (2).pkl', 'rb') as f:
    #     model = pickle.load(f)
    #     # model=model1

    # with open('best_vectorizer (3).pkl', 'rb') as f:
    #     vectorizer = pickle.load(f)
        # vectorizer=vectorizer1