import numpy as np
import csv
import pickle
import pandas as pd

from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from general import load_dataset
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def main():
    with open('smartphone_classifier', 'rb') as classifier:  
        # Load the trained model and X and y values
        model = pickle.load(classifier)
        X, y = load_dataset()

        # Classify as 'smartphone' or 'nao-smartphone'
        y_pred = model.predict(X)

        # Print the results
        print("Matriz de confusao: ")
        print(confusion_matrix(y, y_pred))
        print("Resumo:")  
        print(classification_report(y, y_pred))  
        print("Acuracia:", round((accuracy_score(y, y_pred) * 100), 4), "%") 

        generate_output_file(y_pred)

        return True        

# Generate the output file
def generate_output_file(y_pred):
        output_file = open("output_file.csv", "w+")
        
        # Read the dataset and convert to numpy array
        df = pd.read_csv("data_estag_ds.tsv", sep = "\t")
        dataset = DataFrame.to_numpy(df)
        
        # Write first row
        first_row = "ID TITLE   CLASSIFICATION\n"
        output_file.write(first_row)

        # Append the classifications
        for product in range(len(dataset)):
                document = []
                document.append(str(dataset[product][0]))
                document.append("    ")
                document.append(str(dataset[product][1]))
                document.append("    ")
                document.append(y_pred[product])
                document = ' '.join(document)
                document += "\n"
                
                output_file.write(document)
        
        output_file.close()

        return True        

main()