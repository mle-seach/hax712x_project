# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 19:52:09 2022

@author: Pauline
"""
import csv
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

data = pd.read_csv('eco2mix-national-tr.csv', delimiter=';')

conso = data[['Heure']]
conso = conso.assign(FIOUL_MW=data['Fioul (MW)'])
conso = conso.assign(CHARBON_MW=data['Charbon (MW)'])
conso = conso.assign(GAZ_MW=data['Gaz (MW)'])
conso = conso.assign(Eolien_MW=data['Eolien (MW)'])
conso = conso.assign(Solaire_MW=data['Solaire (MW)'])
conso = conso.assign(Hydraulique_MW=data['Hydraulique (MW)'])
conso = conso.assign(Nucléaire_MW=data['Nucléaire (MW)'])

#print(conso)

conso.dropna(inplace=True)

### Conso de Fioul et de Charbon 
plt.figure()
fioul=conso.groupby(["Heure"])['FIOUL_MW'].mean().plot(color='red')
charbon=conso.groupby(["Heure"])['CHARBON_MW'].mean().plot(color='black')
plt.ylabel('Conso en MW')
plt.legend()


### Conso vent, eau, solaire
plt.figure()
eolien=conso.groupby(["Heure"])['Eolien_MW'].mean().plot(color='chartreuse')
solaire=conso.groupby(["Heure"])['Solaire_MW'].mean().plot(color='orangered')
hydraulique=conso.groupby(["Heure"])['Hydraulique_MW'].mean().plot(color='darkturquoise')
plt.ylabel('Conso en MW')
plt.legend()

### Conso gaz
plt.figure()
gaz=conso.groupby(["Heure"])['GAZ_MW'].mean().plot(color='hotpink')
plt.ylabel('Conso en MW')
plt.legend()

### Conso nucléaire
plt.figure()
nucleaire=conso.groupby(["Heure"])['Nucléaire_MW'].mean().plot(color='midnightblue')
plt.ylabel('Conso en MW')
plt.legend()







#doss=conso.groupby(['Heure']).mean()

#print(doss)



# fig, axes = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

# axes[0].plot(doss['CHARBON_MW'])
# axes[0].set_title("Consommation en MW le 08/12/22")
# axes[0].set_ylabel("Charbon")








