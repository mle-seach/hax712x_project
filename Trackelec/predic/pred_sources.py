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
          'figure.figsize': (15, 10),
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
#print('Estimation consommation de Gaz=',df_gaz)


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
#print('Estimation consommation de Fioul=',df_fioul)


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
#print('Estimation consommation de Charbon=',df_charbon) 


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
#print('Estimation consommation de Nucléaire=',df_nucleaire)


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
#print('Estimation consommation Eolienne=',df_eolien)

df_hydraulique = moy52.to_frame()
#print('Estimation consommation Hydraulique=',df_hydraulique)

df_solaire = moy53.to_frame()
#print('Estimation consommation Solaire=',df_solaire)






#### Comparaison avec le module Prophet ####

# Téléchargement des données de 2022:
url2="https://odre.opendatasoft.com/explore/dataset/eco2mix-national-tr/download/?format=csv&disjunctive.nature=true&q=date_heure:%5B2022-05-31T22:00:00Z+TO+2022-11-29T22:59:59Z%5D&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
path_target = './consommation_2022.csv'
path, fname = os.path.split(path_target)
pooch.retrieve(url2, path=path, fname=fname, known_hash=None)

# Chargement du dataset "consommation.csv"
data1 = pd.read_csv("consommation_2022.csv", delimiter=";", comment="#", na_values="n/d",parse_dates=['Date'], converters={'heure' : str})

# Fonctions pour calculer la différence et la moyenne 
def x(a,b):
    return abs(a - b)

def y(a,b):
    return ((a + b)/2)

# Etude du Gaz 
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
#print('Prediction methode Prophet Gaz=', predic_finale1)

# Creation du dataframe qui contiendra les deux prédictions et leur différence
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
#print(result)


result['abs(D1 - D2)'] = result.apply(lambda f: x(f['D1'],f['D2']), axis=1)
result['Moyenne M1 et M2'] = result.apply(lambda f: y(f['D1'], f['D2']), axis=1)
#print(result)

# calcul de la difference en moyenne 
Diff1 = result['abs(D1 - D2)'].mean()
print('Gaz : En moyenne la différence des deux méthodes est de', Diff1, 'MW')


# Dataframe contenant la moyenne 
moyG = result[["Moyenne M1 et M2"]]


# Affichage graphique 
idee2 = df_gaz1[['Heure']]
idee2 = idee2.assign( moyenne = moyG )
idee2 = idee2.assign( methode1 = result1)
idee2 = idee2.assign( methode2 = result2)

idee2.plot(x='Heure')
plt.title('Comparaison prediction Gaz')


## Etude du Fioul 
df2 = data1.copy()
df2 = data1[['Date', 'Heure', 'Fioul (MW)']]                   
df2 = df2.rename(columns={'Date' : 'ds', 'Fioul (MW)' : 'y'})
df2 = df2.dropna()
df2 = df2.sort_values(by=['ds','Heure'], ascending=(True,True))
df2['ds'] = pd.to_datetime(df2['ds'])
model1 = Prophet()
model1.fit(df2)
f = model1.make_future_dataframe(periods=48*10 , freq='30min', include_history=False)
predic = model1.predict(f)
s = predic[['ds','yhat']]
predic_finale = s[len(s)-49:479]
predic_finale = predic_finale.rename(columns={'ds' : 'Date et Heure', 'yhat' : 'Fioul(MW)'})
#print('Prediction methode Prophet Fioul=', predic_finale)


# Creation du dataframe qui contiendra les deux prédictions et leur différence
df_fioul1 = df_fioul.reset_index()
df_fioul2 = df_fioul1[['Fioul (MW)']]
list_fioul = df_fioul2.to_numpy()
result3 = pd.DataFrame(list_fioul, columns = ['D3'])

fioul = pd.DataFrame(predic_finale)
fioul1 = fioul[['Fioul(MW)']]
list_fioul2 = fioul1.to_numpy()
result4 = pd.DataFrame(list_fioul2, columns = ['D4'])

resultF = result3
resultF = resultF.assign(D4 = result4)
#print(resultF)



resultF['abs(D3 - D4)'] = resultF.apply(lambda f: x(f['D3'],f['D4']), axis=1)
resultF['Moyenne M1 et M2'] = resultF.apply(lambda f: y(f['D3'], f['D4']), axis=1)
#print(resultF)

Diff2 = resultF['abs(D3 - D4)'].mean()

# Dataframe contenant la moyenne 
moyF = resultF[["Moyenne M1 et M2"]]

print('Fioul : En moyenne la différence des deux méthodes est de', Diff2, 'MW')



# Affichage graphique 
idee1 = df_fioul1[['Heure']]
idee1 = idee1.assign( moyenne = moyF )
idee1 = idee1.assign( methode1 = result3)
idee1 = idee1.assign( methode2 = result4)

idee1.plot(x='Heure')
plt.title('Comparaison prediction Fioul')

# Etude de l'Hydraulique
df4 = data1.copy()
df4 = data1[['Date', 'Heure', 'Hydraulique (MW)']]                   
df4 = df4.rename(columns={'Date' : 'ds', 'Hydraulique (MW)' : 'y'})
df4 = df4.dropna()
df4 = df4.sort_values(by=['ds','Heure'], ascending=(True,True))
df4['ds'] = pd.to_datetime(df4['ds'])
model3 = Prophet()
model3.fit(df4)
f3 = model3.make_future_dataframe(periods=48*10 , freq='30min', include_history=False)
predic2 = model3.predict(f3)
s = predic2[['ds','yhat']]
predic_finale2 = s[len(s)-49:479]
predic_finale2 = predic_finale2.rename(columns={'ds' : 'Date et Heure', 'yhat' : 'Hydraulique(MW)'})
#print('Prediction methode Prophet Hydraulique=',predic_finale2)


# Creation du dataframe qui contiendra les deux prédictions et leur différence
df_hyd1 = df_hydraulique.reset_index()
df_hyd2 = df_hyd1[['Hydraulique (MW)']]
list_hyd = df_hyd2.to_numpy()
result5 = pd.DataFrame(list_hyd, columns = ['D5'])

hyd = pd.DataFrame(predic_finale2)
hyd1 = hyd[['Hydraulique(MW)']]
list_hyd2 = hyd1.to_numpy()
result6 = pd.DataFrame(list_hyd2, columns = ['D6'])

resultH = result5
resultH = resultH.assign(D6 = result6)


resultH['abs(D5 - D6)'] = resultH.apply(lambda f: x(f['D5'],f['D6']), axis=1)
resultH['Moyenne M1 et M2'] = resultH.apply(lambda f: y(f['D5'], f['D6']), axis=1)
#print(resultH)

Diff3 = resultH['abs(D5 - D6)'].mean()

# Dataframe contenant la moyenne 
moyH = resultH[["Moyenne M1 et M2"]]

print('Hydarulique : En moyenne la différence des deux méthodes est de', Diff3, 'MW')


# Affichage graphique 
idee3 = df_hyd1[['Heure']]
idee3 = idee3.assign( moyenne = moyH )
idee3 = idee3.assign( methode1 = result5)
idee3 = idee3.assign( methode2 = result6)

idee3.plot(x='Heure')
plt.title('Comparaison prediction Hydraulique')



# Etude du Nucleaire 
df5 = data1.copy()
df5 = data1[['Date', 'Heure', 'Nucléaire (MW)']]                   
df5 = df5.rename(columns={'Date' : 'ds', 'Nucléaire (MW)' : 'y'})
df5 = df5.dropna()
df5 = df5.sort_values(by=['ds','Heure'], ascending=(True,True))
df5['ds'] = pd.to_datetime(df5['ds'])
model4 = Prophet()
model4.fit(df5)
f4 = model4.make_future_dataframe(periods=48*10 , freq='30min', include_history=False)
predic3 = model4.predict(f4)
s = predic3[['ds','yhat']]
predic_finale3 = s[len(s)-49:479]
predic_finale3 = predic_finale3.rename(columns={'ds' : 'Date et Heure', 'yhat' : 'Nucleaire(MW)'})
#print('Prediction methode Prophet Nucleaire =',predic_finale3)


# Creation du dataframe qui contiendra les deux prédictions et leur différence
df_nuc1 = df_nucleaire.reset_index()
df_nuc2 = df_nuc1[['Nucléaire (MW)']]
list_nuc = df_nuc2.to_numpy()
result7 = pd.DataFrame(list_nuc, columns = ['D7'])

nuc = pd.DataFrame(predic_finale3)
nuc1 = nuc[['Nucleaire(MW)']]
list_nuc2 = nuc1.to_numpy()
result8 = pd.DataFrame(list_nuc2, columns = ['D8'])

resultN = result7
resultN = resultN.assign(D8 = result8)



resultN['abs(D7 - D8)'] = resultN.apply(lambda f: x(f['D7'],f['D8']), axis=1)
resultN['Moyenne M1 et M2'] = resultN.apply(lambda f: y(f['D7'], f['D8']), axis=1)
#print(resultN)

Diff4 = resultN['abs(D7 - D8)'].mean()

# Dataframe contenant la moyenne 
moyN = resultN[["Moyenne M1 et M2"]]

print('Nucleaire : En moyenne la différence des deux méthodes est de', Diff4, 'MW')


# Affichage graphique 
idee4 = df_nuc1[['Heure']]
idee4 = idee4.assign( moyenne = moyN )
idee4 = idee4.assign( methode1 = result7)
idee4 = idee4.assign( methode2 = result8)


idee4.plot(x='Heure')
plt.title('Comparaison predictions Nucleaire')

plt.show()