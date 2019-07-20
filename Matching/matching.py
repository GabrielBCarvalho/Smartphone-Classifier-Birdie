# coding: latin-1
import numpy as np
import re
import pandas as pd
import sys
import csv
sys.path.insert(0, '../Classifier')

#from Classifier.general import preprocess, load_dataset_x
import general
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def main():
    # Extract originals datasets and preprocessed datasets
    original_a = read_collected_datas("submarino")
    original_a = clean_original_dataset(original_a)

    original_b = general.load_dataset_x()
    original_b = clean_original_dataset(original_b)

    a = preprocess(original_a)
    b = preprocess(original_b)

    c = np.concatenate((a, b), axis = 0)
    
    # Bag of Words
    vectorizer = CountVectorizer(max_features = 1500, min_df = 5, max_df = 0.7)  
    x = vectorizer.fit_transform(c).toarray()
    x = normalize(x, 1)

    # Auxiliary variables and lists
    len_a = len(a)
    len_b = len(b)
    very_likely_similar = []
    probably_similar = []
    possibly_similar = []

    # Verify similarities
    for i in range(len_a):
        # Item from Submarino dataset
        title_a = x[i]

        for j in range(len_b):
            k = j + len_a

            # Item from given dataset
            title_b = x[k]
            
            # Calculate similarity
            similarity = cosine_similarity(title_a.reshape(1, -1), title_b.reshape(1, -1))

            # If contains a high similarity
            if(similarity >= 0.9):
                print("Similaridade entre: ")
                print("     ", original_a[i][1])
                print("     ", original_b[j][1])
                print("      Similaridade =", similarity, "\n")

                document = [original_a[i][1], original_b[j][1], similarity]
                very_likely_similar.append(document)
            elif(similarity >= 0.8 and similarity < 0.9):     # If contains a good similarity
                document = [original_a[i][1], original_b[j][1], similarity]
                probably_similar.append(document)
            elif(similarity >= 0.7 and similarity < 0.8):      # If contains a fair similarity
                document = [original_a[i][1], original_b[j][1], similarity]
                possibly_similar.append(document)
    
    write_file(very_likely_similar, probably_similar, possibly_similar)


# Read the collected datas from a site
def read_collected_datas(site):
    filename = "../Crawler/collected_datas_" + site + ".tsv"

    # Read the dataset and convert to numpy array
    df = pd.read_csv(filename, sep = "\t", encoding='latin-1', engine='python')
    original_dataset = DataFrame.to_numpy(df)
    
    #dataset = general.preprocess(original_dataset)

    return original_dataset


# Normalize a dataset between 0 and normalize_value
def normalize(dataset, normalize_value):
    # Get the minimum, maximum and range values
    min_value = np.min(dataset)
    max_value = np.max(dataset)
    range_value = max_value - min_value
    # Normalize to [0, 1]
    dataset_normalized = (dataset - min_value) / range_value
    # Normalize to [0, normalize_value]
    dataset_normalized = dataset_normalized * normalize_value

    return dataset_normalized


# Write output file containing pairs and similarities
def write_file(very_likely_similar, probably_similar, possibly_similar):
    with open("matching_titles.tsv", "w+", encoding = 'latin-1') as output_file:
        tsv_writer = csv.writer(output_file, delimiter = "\t")
        tsv_writer.writerow(["TITLE A", "TITLE B", "SIMILARITY"])

        tsv_writer.writerow(["Very likely similars"])
        for item in very_likely_similar:
            tsv_writer.writerow(item)

        tsv_writer.writerow([""])
        tsv_writer.writerow(["Probably similars"])
        for item in probably_similar:
            tsv_writer.writerow(item)

        tsv_writer.writerow([""])
        tsv_writer.writerow(["Possibly similars"])
        for item in possibly_similar:
            tsv_writer.writerow(item)

    print("Created file.")


def clean_original_dataset(original_dataset):
    for i in range (0, len(original_dataset)):
        title = original_dataset[i][1]

        title = title.replace(u"\u00e2", "â")
        title = title.replace("\u201d", '"')
        title = title.replace(u"\u00e1", u"á")
        title = title.replace(u"\u00c1", u"à")
        title = title.replace(u"\u00ed", u"í")
        title = title.replace(u"\u00e9", u"é")
        title = title.replace(u"\u00e7", u"ç")
        title = title.replace(u"\u00e3", u"ã")
        title = title.replace(u"\u00cd", u"I")
        title = title.replace(u"\u00f3", u"ó")
        title = title.replace(u"\u00f5", u"õ")
        title = title.replace(u"\u00ea", u"ê")
        title = title.replace(u"\u00b4", u'"')
        title = title.replace(u"\u00fd", u'y')
        title = title.replace(u"\u00f4", u'ô')
        title = title.replace(u"\u2019\u2019", u'"')
        title = title.replace(u"\u2019", u"'")
        title = title.replace(u"\u2013", u'-')
        title = title.replace(u"\u2122", u'')
        title = title.replace(u"''", u'"')

        original_dataset[i][1] = title

    return original_dataset


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

        # Ignore colors
        document = document.replace("azul", "")
        document = document.replace("rosa", "")
        document = document.replace("dourado", "")
        document = document.replace("amarelo", "")
        document = document.replace("vermelho", "")
        document = document.replace("verde", "")
        document = document.replace("roxo", "")
        document = document.replace("prata", "")
        document = document.replace("preto", "")
        document = document.replace("cinza", "")
        document = document.replace("ametista", "")

        document = document.replace("usado: ", "")
        documents.append(document)
    
    return np.asarray(documents)

main()