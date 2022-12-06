# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 10:47:02 2022

@author: Pauline
"""
import pandas as pd

### Consommation de décembre ###

c2012 = pd.read_csv("d2012.csv", delimiter=";")
c2013 = pd.read_csv("d2013.csv", delimiter=";")
c2014 = pd.read_csv("d2014.csv", delimiter=";")
c2015 = pd.read_csv("d2015.csv", delimiter=";")
c2016 = pd.read_csv("d2016.csv", delimiter=";")
c2017 = pd.read_csv("d2017.csv", delimiter=";")
c2018 = pd.read_csv("d2018.csv", delimiter=";")
c2019 = pd.read_csv("d2019.csv", delimiter=";")
c2020 = pd.read_csv("d2020.csv", delimiter=";")
c2021 = pd.read_csv("d2021.csv", delimiter=";")

# Création d'un dataframe qui contient les valeurs du mois de décembre de chaque année
conso = c2021[["Consommation brute électricité (MW) - RTE"]]
conso.rename(
    columns={"Consommation brute électricité (MW) - RTE": "conso2021"}, inplace=True
)

conso = conso.assign(conso2021=c2021["Consommation brute électricité (MW) - RTE"])
conso = conso.assign(conso2020=c2020["Consommation brute électricité (MW) - RTE"])
conso = conso.assign(conso2019=c2019["Consommation brute électricité (MW) - RTE"])
conso = conso.assign(conso2018=c2018["Consommation brute électricité (MW) - RTE"])
conso = conso.assign(conso2017=c2017["Consommation brute électricité (MW) - RTE"])
conso = conso.assign(conso2016=c2016["Consommation brute électricité (MW) - RTE"])
conso = conso.assign(conso2015=c2015["Consommation brute électricité (MW) - RTE"])
conso = conso.assign(conso2014=c2014["Consommation brute électricité (MW) - RTE"])
conso = conso.assign(conso2013=c2013["Consommation brute électricité (MW) - RTE"])
conso = conso.assign(conso2012=c2012["Consommation brute électricité (MW) - RTE"])

# print('Consommations=')
print(conso)

moy = conso.mean(axis=1)
# print('Moyenne des consommations par jour/heure=', moy)


moy2 = moy.to_frame()
# print(moy2)

data0 = c2020[["Heure"]]
data0 = data0.assign(moyenne=moy2[0])
# print(data0)

doss = data0.groupby(["Heure"]).mean()
print("doss=", doss)
