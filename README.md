# movie_review_analyser_nlp
IMDB Sentiment Classifier (Command Line Tool)
This project is a simple sentiment analysis tool built using Python. It takes a movie review as input and tells whether the sentiment is positive or negative. It uses a trained Logistic Regression model and a TF-IDF vectorizer saved in pickle format.



What it does
Takes in a text review via the command line.

Converts it to a vector using the TF-IDF vectorizer.

Uses the Logistic Regression model to predict if the sentiment is positive or negative.

Prints the result in the terminal.





Files in the Project
predict.py - Main script that takes input from the command line and prints prediction.

logreg_imdb.pkl - Trained Logistic Regression model saved using pickle.

tfidf_vectorizer.pkl - TF-IDF vectorizer used to preprocess input text.

nlp.ipynb - Jupyter Notebook used to train and save the model and vectorizer.





How to Run
Clone or download this project folder.

Open terminal or Git Bash inside the folder.

Install the required libraries:
pip install textblob scikit-learn
Run the script with your input text:
python predict.py "This movie was amazing and thrilling"
Output will be:
Prediction: positive




Behind the Scenes
The input text is vectorized using the same TF-IDF settings that were used during training.

The Logistic Regression model takes this vector and predicts the sentiment.

Both the vectorizer and model are loaded from .pkl files to keep the script lightweight and fast.

Notes
The model was trained on IMDB movie reviews.

Only English text is supported.

Works fully offline once dependencies are installed.
