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
from prophet import Prophet

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
path_target = './consommation4.csv'
path, fname = os.path.split(path_target)
pooch.retrieve(url, path=path, fname=fname, known_hash=None)

# Préparation de notre jeu de données
cons = pd.read_csv("consommation4.csv", sep=";")

cons = cons.set_index('Date')
#print(cons.head(10))

data = cons.loc[[ "2020-12-08", "2019-12-08", "2018-12-08", "2017-12-08"
                 , "2016-12-08", "2015-12-08", "2014-12-08", "2013-12-08"
                 , "2012-12-08"]]
#print(data)

## Valeurs véritables Gaz ##
data2022 = cons.loc[["2021-12-08"]]
vrai1 = data2022[['Heure', 'Gaz (MW)']]
vrai1.dropna(inplace = True)
vrai1 = vrai1.sort_values(by='Heure', ascending=True)
vrai1.set_index('Heure', inplace=True)
#print(vrai1)



## Etude du Gaz avec la moyenne ##
data1 = data[['Heure', 'Gaz (MW)']]
data1.dropna(inplace = True)
data1 = data1.sort_values(by='Heure', ascending=True)
data1.set_index('Heure', inplace=True)
#print(data1)
moy1 = data1.groupby(["Heure"])['Gaz (MW)'].mean()
#print(moy1)

fig, ax2 = plt.subplots()

ax2.plot(moy1, label = 'Methode1')
ax2.plot(vrai1, label = 'Vérité')
plt.xticks(rotation = 'vertical' )
plt.title('Prédiction conso en MW le 08/12/21')
plt.legend()

#%%
## Etude du Gaz avec Prophet ##
url2="https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/download/?format=csv&disjunctive.nature=true&q=date_heure:%5B2020-12-31T23:00:00Z+TO+2021-11-30T22:59:59Z%5D&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
path_target = './consommation_2021.csv'
path, fname = os.path.split(path_target)
pooch.retrieve(url2, path=path, fname=fname, known_hash=None)
data1 = pd.read_csv("consommation_2021.csv", delimiter=";", comment="#", na_values="n/d",parse_dates=['Date'], converters={'heure' : str})

df3 = data1.copy()
df3 = data1[['Date', 'Heure', 'Gaz (MW)']]                   
df3 = df3.rename(columns={'Date' : 'ds', 'Gaz (MW)' : 'y'})
df3 = df3.dropna()
df3 = df3.sort_values(by=['ds','Heure'], ascending=(True,True))
df3['ds'] = pd.to_datetime(df3['ds'])
model2 = Prophet()
model2.fit(df3)
f2 = model2.make_future_dataframe(periods=48*10 , freq='30min', include_history=False)
predic1 = model2.predict(f2)
s = predic1[['ds','yhat']]
predic_finale1 = s[len(s)-49:479]
predic_finale1 = predic_finale1.rename(columns={'ds' : 'Date et Heure', 'yhat' : 'Gaz(MW)'})


jj = vrai1.reset_index()
jj = jj.drop(['Gaz (MW)'], axis=1)

list_gaz = jj.to_numpy()
result1 = pd.DataFrame(list_gaz, columns = ['Heure'])
gaz = pd.DataFrame(predic_finale1)
gaz1 = gaz[['Gaz(MW)']]
list_gaz2 = gaz1.to_numpy()
result2 = pd.DataFrame(list_gaz2, columns = ['Methode2'])
met2 = result1
met2 = met2.assign(Methode2 = result2)
met2.set_index('Heure', inplace=True)
#print(met2)

fig, ax3 = plt.subplots()

ax3.plot(met2, label = 'Methode2')
ax3.plot(vrai1, label = 'Vérité')
plt.xticks(rotation = 'vertical' )
plt.title('Prédiction conso en MW le 08/12/21')
plt.legend()


#%%
def y(a,b):
    return ((a + b)/2)

def x(a,b):
    return abs(a - b)


df_gaz = moy1.to_frame()
df_gaz1 = df_gaz.reset_index()
df_gaz2 = df_gaz1[['Gaz (MW)']]
list_gaz = df_gaz2.to_numpy()
result1 = pd.DataFrame(list_gaz, columns = ['D1'])
gaz = pd.DataFrame(predic_finale1)
gaz1 = gaz[['Gaz(MW)']]
list_gaz2 = gaz1.to_numpy()
result2 = pd.DataFrame(list_gaz2, columns = ['D2'])
result = result1
result = result.assign(D2 = result2)

result['abs(D1 - D2)'] = result.apply(lambda f: x(f['D1'],f['D2']), axis=1)
result['Moyenne M1 et M2'] = result.apply(lambda f: y(f['D1'], f['D2']), axis=1)
moyG = result[["Moyenne M1 et M2"]]


oo = vrai1.reset_index()
compa = result[['D1', 'D2', 'Moyenne M1 et M2']]
compa = compa.assign( vrai = oo['Gaz (MW)'] )

compa['vrai -1']= compa.apply(lambda f: x(f['D1'],f['vrai']), axis=1)
compa['vrai -2']= compa.apply(lambda f: x(f['D2'],f['vrai']), axis=1)
compa['vrai -3']= compa.apply(lambda f: x(f['Moyenne M1 et M2'],f['vrai']), axis=1)

Diff1 = compa['vrai -1'].mean()
Diff2 = compa['vrai -2'].mean()
Diff3 = compa['vrai -3'].mean()

print(Diff1)

print(Diff2)

print(Diff3)

fig, ax4 = plt.subplots()

ax4.plot(moyG, label = 'Methode3')
ax4.plot(vrai1, label = 'Vérité')
plt.xticks(rotation = 'vertical' )
plt.title('Prédiction conso en MW le 08/12/21')
plt.legend()

#%%
fig, ax = plt.subplots()

ax.plot(moy1, label = 'Methode1')
ax.plot(vrai1, label = 'Vérité')
ax.plot(met2, label = 'Methode2')
ax.plot(moyG, label = 'Moyenne des deux méthodes')
plt.xticks(rotation = 'vertical' )
plt.title('Prédiction conso GAZ en MW le 08/12/21')
plt.legend()
plt.show()


