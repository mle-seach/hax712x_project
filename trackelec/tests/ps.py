import os

import pandas as pd
import pooch

url = "https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
path_target = "./consommation3.csv"
path, fname = os.path.split(path_target)
pooch.retrieve(url, path=path, fname=fname, known_hash=None)

data = pd.read_csv("consommation3.csv", sep=";")

conso1 = data.copy()
conso1 = conso1[["Date", "Nucléaire (MW)", "Gaz (MW)"]]
conso1 = conso1.set_index("Date")
conso1.dropna(inplace=True)
NG = conso1.iloc[1, 0]
NN = conso1.iloc[6, 1]
# print(NG)
# print(NN)

conso2 = data.copy()
conso2 = conso2[["Date", "Charbon (MW)", "Fioul (MW)"]]
conso2 = conso2.set_index("Date")
conso2.dropna(inplace=True)
NC = conso2.iloc[9, 0]
NF = conso2.iloc[20, 1]


# print(NC)
# print(NF)


def don1(x):
    return x + NG


def don2(x):
    return x + NN


def don3(x):
    return x + NC


def don4(x):
    return x + NF
