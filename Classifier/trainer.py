import numpy as np
import csv
import pickle

from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from general import load_dataset
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


def main():
    # Loading dataset
    X, y = load_dataset()

    # Training the classifier
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0, stratify = y)
    classifier = RandomForestClassifier(n_estimators = 1000, random_state = 0)  
    classifier.fit(X_train, y_train.ravel()) 

    # Predicting values 
    y_pred = classifier.predict(X_test)

    # Print results
    print("Matriz de confusao: ")
    print(confusion_matrix(y_test, y_pred))
    print("Resumo:")  
    print(classification_report(y_test, y_pred))  
    print("Acuracia:", round(accuracy_score(y_test, y_pred), 4) * 100, "%") 

    # Saving the model
    with open('smartphone_classifier', 'wb') as pickle_file:  
        pickle.dump(classifier, pickle_file)

        
main()