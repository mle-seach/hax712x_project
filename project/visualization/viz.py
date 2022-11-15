import os
import datetime

from download import download
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
from urllib import request
import json

# Data cleaning
# TODO look for missing data, separate per year

url = 'https://data.enedis.fr/explore/dataset/consommation-annuell  e-residentielle-par-adresse/download'
data_path = os.path.join(os.getcwd(), 'data_viz.csv')
path = download(url, data_path, progressbar=True, verbose=True)

df = pd.read_csv(data_path, sep=";")
df.drop(['code_iris', 'nom_iris', 'numero_de_voie', 'indice_de_repetition', 'type_de_voie', 'libelle_de_voie',
         'segment_de_client', 'adresse', 'tri_des_adresses'], axis=1, inplace=True)

city = 'https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/communes-version-simplifiee.geojson'
dept = 'https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements-version-simplifiee.geojson'
region = 'https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/regions-version-simplifiee.geojson'

# Plots
# TODO Violin plot per year


# Interactive map
# TODO violin plot when hovering over city, define class with its methods for the map
# Beaucoup de villes manquantes...

def read_geojson(url):
    with request.urlopen(url) as url:
        jdata = json.loads(url.read().decode())
    return jdata


jdata = read_geojson(city)

fig = px.choropleth_mapbox(df, geojson=jdata,
                           featureidkey='properties.code',
                           locations='code_commune',
                           color='consommation_annuelle_moyenne_de_la_commune_mwh',
                           animation_frame='annee',
                           color_continuous_scale='viridis',
                           zoom=4.5,
                           mapbox_style='carto-positron')

fig.update_layout(title_text='Consommation annuelle moyenne de la commune par habitant',
                  title_x=0.5,
                  coloraxis_colorscale='viridis',
                  mapbox=dict(style='carto-positron',
                              zoom=4.5,
                              center={"lat": 46.2276, "lon": 2.2137},
                              ))
fig.show()
