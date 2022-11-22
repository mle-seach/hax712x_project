# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:30:59 2022

@author: Pauline
"""
import pandas as pd
import pooch 
import os
import matplotlib.pyplot as plt
import pylab

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

# Préparation de notre jeu de données
cons = pd.read_csv("consommation3.csv", sep=";")

cons = cons.set_index('Date')
#print(cons.head(10))

data = cons.loc[["2021-12-08", "2020-12-08", "2019-12-08", "2018-12-08", "2017-12-08"
                 , "2016-12-08", "2015-12-08", "2014-12-08", "2013-12-08"
                 , "2012-12-08"]]
#print(data)


## Etude du Gaz ##
data1 = data[['Heure', 'Gaz (MW)']]
data1.dropna(inplace = True)
data1 = data1.sort_values(by='Heure', ascending=True)
data1.set_index('Heure', inplace=True)
#print(data1)
moy1 = data1.groupby(["Heure"])['Gaz (MW)'].mean()

plt.figure()
Gaz = moy1.plot(color='hotpink')
plt.title('Prédiction conso en MW le 08/12/22')
plt.legend()

df_gaz = moy1.to_frame()
df_gaz




## Etude du Fioul ##
data2 = data[['Heure', 'Fioul (MW)']]
data2.dropna(inplace = True)
data2 = data2.sort_values(by='Heure', ascending=True)
data2.set_index('Heure', inplace=True)
#print(data2)
moy2 = data2.groupby(["Heure"])['Fioul (MW)'].mean()

plt.figure()
Fioul = moy2.plot(color='red')
plt.title('Prédiction conso en MW le 08/12/22')
plt.legend()

df_fioul = moy2.to_frame()
df_fioul

## Etude du Charbon ##
data3 = data[['Heure', 'Charbon (MW)']]
data3.dropna(inplace = True)
data3 = data3.sort_values(by='Heure', ascending=True)
data3.set_index('Heure', inplace=True)
#print(data3)
moy3 = data3.groupby(["Heure"])['Charbon (MW)'].mean()

plt.figure()
Charbon = moy3.plot(color='black')
plt.title('Prédiction conso en MW le 08/12/22')
plt.legend()

df_charbon = moy3.to_frame()
df_charbon 

## Etude du Nucléaire ##
data4 = data[['Heure', 'Nucléaire (MW)']]
data4.dropna(inplace = True)
data4 = data4.sort_values(by='Heure', ascending=True)
data4.set_index('Heure', inplace=True)
#print(data4)
moy4 = data4.groupby(["Heure"])['Nucléaire (MW)'].mean()

plt.figure()
Nucléaire = moy4.plot(color='midnightblue')
plt.title('Prédiction conso en MW le 08/12/22')
plt.legend()

df_nucleaire = moy4.to_frame()
df_nucleaire


## Etude de l'Eolien, de l'Hydraulique et du Solaire ##
data5 = data[['Heure', 'Eolien (MW)', 'Hydraulique (MW)', 'Solaire (MW)']]
data5.dropna(inplace = True)
data5 = data5.sort_values(by='Heure', ascending=True)
data5.set_index('Heure', inplace=True)
#print(data5)
moy51 = data5.groupby(["Heure"])['Eolien (MW)'].mean()
moy52 = data5.groupby(["Heure"])['Hydraulique (MW)'].mean()
moy53 = data5.groupby(["Heure"])['Solaire (MW)'].mean()

plt.figure()
Eolien = moy51.plot(color='chartreuse')
Hydraulique = moy52.plot(color='darkturquoise')
Solaire = moy53.plot(color='orangered')
plt.title('Prédiction conso en MW le 08/12/22')
plt.legend()

df_eolien = moy51.to_frame()
df_eolien

df_hydraulique = moy52.to_frame()
df_hydraulique

df_solaire = moy53.to_frame()
df_solaire
