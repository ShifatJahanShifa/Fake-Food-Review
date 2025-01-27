# Bangla Fake Food Review Detection System
A Bangla Fake Food Review Detection System is a technological solution designed to identify and filter fake or deceptive reviews in the Bangla language, Romanized Bangla language related to food items. It leverages natural language processing (NLP) techniques, machine learning algorithms, and sentiment analysis to distinguish between authentic and fraudulent reviews.

## Browser Extension
We have made a browser extension for using our model to detect fake food review. Currently the extension is available for localhost server. Very soon we will deploy our server.

## AI Methods 🛠️

### Natural Language Processing (NLP) 🌐
- **Text Conversion & Preprocessing**: Tokenization, stop-word removal, stemming, lemmatization, and normalization.
- **Augmentation Tools**: `nlpaug` and `bnaug` are used for dataset diversification.

---

## Machine Learning Models Utilized 🛠️
The project implements the following algorithms to ensure robust predictions:  

- **Logistic Regression**  
- **Decision Tree**  
- **Random Forest**  
- **Gradient Boosting**  
- **Extra Trees**  
- **AdaBoost**  
- **XGBoost**  
- **K-Nearest Neighbors (KNN)**  
- **Linear Support Vector Machine (Linear SVM)**  
- **Radial Basis Function SVM (RBF SVM)**  
- **Stochastic Gradient Descent (SGD)**  

---

## Workflow 🔄

1. **Input 📝**: User-submitted Bengali review.
2. **Preprocessing 🧹**:
   - Tokenization, stop-word removal, stemming, and lemmatization.
   - Text augmentation for diverse training samples.
3. **Feature Engineering**: Extract linguistic, semantic, and behavioral features.
4. **Model Training 🧠**: Apply and compare multiple machine learning algorithms for classification.
5. **Output ✅**: Label the review as `fake` or `genuine` with confidence scores.

---

## We are planning to implement deep learning models also!!!!
### Deep Learning Models 🧠
- **CNN & LSTM**:
  - Convolutional Neural Networks (CNNs) identify spatial patterns in embeddings.
  - Long Short-Term Memory (LSTM) networks capture sequential dependencies.
  - **Attention Mechanism**: Highlights critical parts of the text for better interpretability.
- **Transformer Models**:
  - Pre-trained models like **Bangla BERT** and **sahajBERT** understand the deep context and semantics of Bengali text.
- **Ensemble Learning**:
  - Combines CNN, LSTM, and transformers for improved accuracy and robustness.

---

## Dataset 📂

- **Primary Dataset**: [Bengali Fake Reviews Dataset](https://www.kaggle.com/datasets/shawontanvir/bengali-fake-review-dataset) from Kaggle.
- **Additional Data**: User-generated reviews from public platforms.

---
