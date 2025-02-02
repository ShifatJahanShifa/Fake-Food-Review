import pickle

# Load the model
with open('best_model_hoi (4).pkl', 'rb') as file:
    model = pickle.load(file)

# Example sentence

sentence = " #অফার🐒🐒🤩ও ভাই। স্লোগান দিয়েন নাহ।🙊 সামনে ১৪ই ফেব্রুয়ারি 😜তাই ১২০টাকার ভালোবাসাই আমার সম্বল। Banglalink Digital অপারেটর Tamim Mridha কে দিয়ে চাপা মারাইয়া গেলো মাই বাংলালিংক সিম আসলে পাবি, ১০০তে তুই ১২০😍বাংলালিংক সিম কিনিলাম!😒কিন্তু চাপা তো চাপাই রয়ে গেলো। 🤭শুধুমাত্র কথা দিয়ে কথা রাখলো Gaggan food । ১২০টার অফার দিয়ে ১২০টাকাই রাখলো😁 🎀তাই আমিও খেয়ে দিলাম তাদের এই ১২০টাকার #রাইস_বোউল। যার সাথে থাকছেঃ🚩বোউল ভরা রাইস।🏋🚩নাগা বিবিকিউ চিকেন।🌶🚩সালাদ।🐸ভালোই ছিলো।😊 "
with open('best_vectorizer_hoi (4).pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Transform the input sentence
sentence_vectorized = vectorizer.transform([sentence])

# Get prediction
prediction = model.predict(sentence_vectorized)

print("Prediction:", prediction[0])