# -*- coding: utf-8 -*-
"""
Created on Mon Nov 7 12:42:23 2022

@author: sarah
"""
import os

# Importer les packages nécessaires:
import pandas as pd
import pooch

# %%
# Données de la consommation d'électricité pour le 08 décembre 2012

# Créer le fichier 'consommation2012.csv' à partit de l'url
url1 = "https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/download/?format=csv&disjunctive.nature=true&refine.date_heure=2012&q=date_heure:%5B2012-12-07T23:00:00Z+TO+2012-12-08T22:59:59Z%5D&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"  # noqa
path_target = './consommation2012.csv'
path, fname = os.path.split(path_target)
pooch.retrieve(url1, path=path, fname=fname, known_hash=None)

# Visualisation des données
df_1 = pd.read_csv("consommation2012.csv", delimiter=";", comment="#",
                   na_values="n/d")
df1 = df_1[['Date', 'Heure', 'Consommation (MW)']]
df1 = df1.dropna()
df1 = df1.sort_values(by='Heure', ascending=True)  # Ordonner les heures:

# %%
# Consommation d'électricité pour le 08 décembre 2013
url2 = "https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/download/?format=csv&disjunctive.nature=true&refine.date_heure=2013&q=date_heure:%5B2013-12-07T23:00:00Z+TO+2013-12-08T22:59:59Z%5D&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"  # noqa
path_target = './consommation2013.csv'
path, fname = os.path.split(path_target)
pooch.retrieve(url2, path=path, fname=fname, known_hash=None)

# Visualisation des données :
df_2 = pd.read_csv("consommation2013.csv", delimiter=";", comment="#",
                   na_values="n/d")
df2 = df_2[['Date', 'Heure', 'Consommation (MW)']]
df2 = df2.dropna()
df2 = df2.sort_values(by='Heure', ascending=True)  # Ordonner les heures

# %%
# Consommation d'électricité pour le 08 décembre 2014:
url3 = "https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/download/?format=csv&disjunctive.nature=true&refine.date_heure=2014&q=date_heure:%5B2014-12-07T23:00:00Z+TO+2014-12-08T22:59:59Z%5D&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"  # noqa
path_target = './consommation2014.csv'
path, fname = os.path.split(path_target)
pooch.retrieve(url3, path=path, fname=fname, known_hash=None)

# Visualisation des données :
df_3 = pd.read_csv("consommation2014.csv", delimiter=";", comment="#",
                   na_values="n/d")
df3 = df_3[['Date', 'Heure', 'Consommation (MW)']]
df3 = df3.dropna()
df3 = df3.sort_values(by='Heure', ascending=True)  # Ordonner les heures

# %%
# Consommation d'électricité pour le 08 décembre 2015:
url4 = "https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/download/?format=csv&disjunctive.nature=true&refine.date_heure=2015%2F12%2F08&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"  # noqa
path_target = './consommation2015.csv'
path, fname = os.path.split(path_target)
pooch.retrieve(url4, path=path, fname=fname, known_hash=None)

# Visualisation des données :
df_4 = pd.read_csv("consommation2015.csv", delimiter=";", comment="#",
                   na_values="n/d")
df4 = df_4[['Date', 'Heure', 'Consommation (MW)']]
df4 = df4.dropna()
df4 = df4.sort_values(by='Heure', ascending=True)  # Ordonner les heures
# %%
# Consommation d'électricité pour le 08 décembre 2016:
url5 = "https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/download/?format=csv&disjunctive.nature=true&refine.date_heure=2016%2F12%2F08&q=date_heure:%5B2016-12-07T23:00:00Z+TO+2016-12-08T22:59:59Z%5D&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"  # noqa
path_target = './consommation2016.csv'
path, fname = os.path.split(path_target)
pooch.retrieve(url5, path=path, fname=fname, known_hash=None)

# Visualisation des données :
df_5 = pd.read_csv("consommation2016.csv", delimiter=";", comment="#",
                   na_values="n/d")
df5 = df_5[['Date', 'Heure', 'Consommation (MW)']]
df5 = df5.dropna()
df5 = df5.sort_values(by='Heure', ascending=True)  # Ordonner les heures

# %%
# Consommation d'électricité pour le 08 décembre 2017:
url6 = "https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/download/?format=csv&disjunctive.nature=true&refine.date_heure=2017%2F12%2F08&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"  # noqa
path_target = './consommation2017.csv'
path, fname = os.path.split(path_target)
pooch.retrieve(url6, path=path, fname=fname, known_hash=None)

# Visualisation des données :
df_6 = pd.read_csv("consommation2017.csv", delimiter=";", comment="#",
                   na_values="n/d")
df6 = df_6[['Date', 'Heure', 'Consommation (MW)']]
df6 = df6.dropna()
df6 = df6.sort_values(by='Heure', ascending=True)  # Ordonner les heures
# %%
# Consommation d'électricité pour le 08 décembre 2018:
url7 = "https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/download/?format=csv&disjunctive.nature=true&refine.date_heure=2018%2F12%2F08&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"  # noqa
path_target = './consommation2018.csv'
path, fname = os.path.split(path_target)
pooch.retrieve(url7, path=path, fname=fname, known_hash=None)

# Visualisation des données :
df_7 = pd.read_csv("consommation2018.csv", delimiter=";", comment="#",
                   na_values="n/d")
df7 = df_7[['Date', 'Heure', 'Consommation (MW)']]
df7 = df7.dropna()
df7 = df7.sort_values(by='Heure', ascending=True)  # Ordonner les heures
# %%
# Consommation d'électricité pour le 08 décembre 2019:
url8 = "https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/download/?format=csv&disjunctive.nature=true&refine.date_heure=2019%2F12%2F08&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"  # noqa
path_target = './consommation2019.csv'
path, fname = os.path.split(path_target)
pooch.retrieve(url8, path=path, fname=fname, known_hash=None)

# Visualisation des données :
df_8 = pd.read_csv("consommation2019.csv", delimiter=";", comment="#",
                   na_values="n/d")
df8 = df_8[['Date', 'Heure', 'Consommation (MW)']]
df8 = df8.dropna()
df8 = df8.sort_values(by='Heure', ascending=True)  # Ordonner les heures

# %%
# Consommation d'électricité pour le 08 décembre 2020:
url9 = "https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/download/?format=csv&disjunctive.nature=true&refine.date_heure=2020%2F12%2F08&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"  # noqa
path_target = './consommation2020.csv'
path, fname = os.path.split(path_target)
pooch.retrieve(url9, path=path, fname=fname, known_hash=None)

# Visualisation des données :
df_9 = pd.read_csv("consommation2020.csv", delimiter=";", comment="#",
                   na_values="n/d")
df9 = df_9[['Date', 'Heure', 'Consommation (MW)']]
df9 = df9.dropna()
df9 = df9.sort_values(by='Heure', ascending=True)  # Ordonner les heures

# %%
# Consommation d'électricité pour le 08 décembre 2021:
url10 = "https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/download/?format=csv&disjunctive.nature=true&refine.date_heure=2021%2F12%2F08&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"  # noqa
path_target = './consommation2021.csv'
path, fname = os.path.split(path_target)
pooch.retrieve(url10, path=path, fname=fname, known_hash=None)

# Visualisation des données :
df_10 = pd.read_csv("consommation2021.csv", delimiter=";", comment="#",
                    na_values="n/d")
df10 = df_10[['Date', 'Heure', 'Consommation (MW)']]
df10 = df10.dropna()
df10 = df10.sort_values(by='Heure', ascending=True)  # Ordonner les heures

# %%
# Regrouper toutes les données dans le même dataframe:
df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10], axis=0)
print(df)
