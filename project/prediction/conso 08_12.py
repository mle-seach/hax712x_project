# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 11:31:34 2022

@author: Pauline
"""
import numpy as np
import pandas as pd

### Consommation du 08 décembre ###

c2012 = pd.read_csv("2012.csv", delimiter=";")
c2013 = pd.read_csv("2013.csv", delimiter=";")
c2014 = pd.read_csv("2014.csv", delimiter=";")
c2015 = pd.read_csv("2015.csv", delimiter=";")
c2016 = pd.read_csv("2016.csv", delimiter=";")
c2017 = pd.read_csv("2017.csv", delimiter=";")
c2018 = pd.read_csv("2018.csv", delimiter=";")
c2019 = pd.read_csv("2019.csv", delimiter=";")
c2020 = pd.read_csv("2020.csv", delimiter=";")
c2021 = pd.read_csv("2021.csv", delimiter=";")

# Création d'un dataframe qui contient les valeurs du 08/12 de chaque année
conso = c2021[["Consommation brute électricité (MW) - RTE", "Heure"]]
conso.rename(
    columns={"Consommation brute électricité (MW) - RTE": "conso2021"}, inplace=True
)

conso = conso.assign(conso2020=c2020["Consommation brute électricité (MW) - RTE"])
conso = conso.assign(conso2019=c2019["Consommation brute électricité (MW) - RTE"])
conso = conso.assign(conso2018=c2018["Consommation brute électricité (MW) - RTE"])
conso = conso.assign(conso2017=c2017["Consommation brute électricité (MW) - RTE"])
conso = conso.assign(conso2016=c2016["Consommation brute électricité (MW) - RTE"])
conso = conso.assign(conso2015=c2015["Consommation brute électricité (MW) - RTE"])
conso = conso.assign(conso2014=c2014["Consommation brute électricité (MW) - RTE"])
conso = conso.assign(conso2013=c2013["Consommation brute électricité (MW) - RTE"])
conso = conso.assign(conso2012=c2012["Consommation brute électricité (MW) - RTE"])

print("Consommations=")
print(conso)

conso.set_index("Heure", inplace=True)

moy = conso.mean(axis=1)
np.round(moy, 2)
print("Moyenne des consommations=")
print(moy)
