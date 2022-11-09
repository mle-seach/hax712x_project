# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 12:42:23 2022

@author: sarah
"""

#Importer les packages nécessaires:

import pandas as pd
import numpy as np
import pooch 
import os
import matplotlib.pyplot as plt
from datetime import datetime 


#%%
#Créer le fichier 'consommation.csv' à partit de l'url

url = "https://www.data.gouv.fr/fr/datasets/r/72c72414-a2d8-4dc5-b699-ff70eb6b4c4c"
path_target = './consommation.csv'
path, fname = os.path.split(path_target)
pooch.retrieve(url, path=path, fname=fname, known_hash=None)


# Visualisation des données
df1 = pd.read_csv("consommation.csv", delimiter=";", comment="#", na_values="n/d", parse_dates=['date'])
print(df1)

#%% 
#Selectionner les colonnes utiles

df_cons = df1[['date', 'heure', 'consommation']]
df_cons = df_cons.rename(columns = {'date':'Date', 'heure':'Heure', 'consommation':'Consommation (MW)'}) 
df_cons = df_cons.dropna(axis=0) #supprimer les valeurs manquantes
df_cons = df_cons.set_index('Date')
#print(df_cons.index)
df_cons.index = pd.to_datetime(df_cons.index) # convertir l'objet 'date' de string à datetime
df_cons = df_cons.sort_values(by='Date', ascending=True) #trier le dataframe dans l'ordre croissant

print(df_cons.head(10))
print(df_cons.tail(10))

#%%
#Visualiser les données:
df_cons.plot(style='.', figsize=(20, 5), title="Consommation d'électricité en France (MW)")
plt.savefig("consommation_electricite.pdf")



