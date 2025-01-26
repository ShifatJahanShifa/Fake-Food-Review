from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from flask_cors import CORS
import dill as pickle


app = Flask(__name__)
CORS(app)

try:
    with open('best_model_hoi.pkl', 'rb') as f:
        model = pickle.load(f)
except (FileNotFoundError, pickle.UnpicklingError) as e:
    model = None
    print(f"Error loading model: {e}")

try:
    with open('best_vectorizer_hoi.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
except (FileNotFoundError, pickle.UnpicklingError) as e:
    vectorizer = None
    print(f"Error loading vectorizer: {e}")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get('text')
    if text is not None:
        text_transformed = vectorizer.transform([text])

        prediction = model.predict(text_transformed)[0]

        return jsonify({'prediction': int(prediction)})
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