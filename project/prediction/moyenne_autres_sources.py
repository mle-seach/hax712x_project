# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 20:06:02 2022

@author: Pauline
"""
import pandas as pd
import matplotlib.pyplot as plt
import pylab
import numpy as np
import pooch 
import os
from datetime import datetime

# Paramètres d'affichage
pylab.style.use('fivethirtyeight') 
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (20, 10),
          'lines.linewidth': 1.5,
          'axes.labelsize': 'x-large',
          'axes.titlesize':35,
          'axes.titleweight':'bold',
          'xtick.labelsize':'x-large',
          'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

url = "https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B" 
path_target = './consommation3.csv'
path, fname = os.path.split(path_target)
pooch.retrieve(url, path=path, fname=fname, known_hash=None)


# Visualisation des données
data = pd.read_csv("consommation3.csv", sep=";")
#print(data.head(10))

# Creation de notre jeu de données et nettoyage
conso1 = data.copy()
conso1 = conso1[['Date', 'Nucléaire (MW)', 'Gaz (MW)']]
conso1.dropna(inplace=True)

conso2 = data.copy()
conso2 = conso2[['Date', 'Charbon (MW)', 'Fioul (MW)']]
conso2.dropna(inplace=True)

conso3 = data.copy()
conso3 = conso3[['Date', 'Eolien (MW)', 'Solaire (MW)', 'Hydraulique (MW)']]
conso3.dropna(inplace=True)



conso1['Date'] = pd.to_datetime(conso1['Date'])
conso1.set_index('Date', inplace=True)
#print(conso1)

conso2['Date'] = pd.to_datetime(conso2['Date'])
conso2.set_index('Date', inplace=True)
#print(conso2)

conso3['Date'] = pd.to_datetime(conso3['Date'])
conso3.set_index('Date', inplace=True)
#print(conso3)

# On regroupe les données par jour
daily_groups1 = conso1.resample('D')
daily_data1 = daily_groups1.mean()
daily_data1.columns = ['Nucléaire','Gaz']
#print(daily_data1)

daily_groups2 = conso2.resample('D')
daily_data2 = daily_groups2.mean()
daily_data2.columns = ['Charbon', 'Fioul']
#print(daily_data2)

daily_groups3 = conso3.resample('D')
daily_data3 = daily_groups3.mean()
daily_data3.columns = ['Eolien', 'Solaire', 'Hydraulique' ]
#print(daily_data3)



# Affichage des données
ax = daily_data1.plot(title='Consommation moyenne en MW', figsize=(15,7))
ax = daily_data2.plot(title='Consommation moyenne en MW', figsize=(15,7))
ax = daily_data3.plot(title='Consommation moyenne en MW', figsize=(15,7))




