
import joblib
import re
import sys

model = joblib.load("logreg_imdb.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

text = sys.argv[1]
text_clean = re.sub(r"[^a-zA-Z]", " ", text.lower())
vect_text = vectorizer.transform([text_clean])
pred = model.predict(vect_text)
print("Prediction:", pred[0])
