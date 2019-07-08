import numpy as np
import re
import pandas as pd

from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer


def load_dataset():
    # Read the dataset and convert to numpy array
    df = pd.read_csv("data_estag_ds.tsv", sep = "\t")
    dataset = DataFrame.to_numpy(df)
    
    # Preprocess the dataset entries
    X = preprocess(dataset)

    # Products classes
    y = pd.read_csv("y_file.csv", header = None)
    y = y.values
    
    # Bag of Words
    vectorizer = CountVectorizer(max_features = 1500, min_df = 5, max_df = 0.7)  
    X = vectorizer.fit_transform(X).toarray()

    return X, y


# Preprocess a given dataset
def preprocess(dataset):
    documents = []

    for product in range(len(dataset)):
        document = dataset[product][1]

        # Remove single '/' and '-' characters
        document = re.sub(r'\s+[/]\s+', ' ', document)
        document = re.sub(r'\s+[-]\s+', ' ', document)

        # Removing special characters
        document = document.replace(",", " ")
        document = document.replace("|", " ")
        document = document.replace("/", " ")
        document = document.replace(",", " ")

        # Substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)
        
        # Convert to lowercase
        document = document.lower()

        documents.append(document)
    
    return np.asarray(documents)