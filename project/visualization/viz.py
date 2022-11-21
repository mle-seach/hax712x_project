import os

from download import download
import pandas as pd
import plotly.express as px
import json
import seaborn as sns
import matplotlib.pyplot as plt
from dash import Dash, dcc, html, Input, Output


# Downloading data
url = 'https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/download'
data_path = os.path.join(os.getcwd(), 'data_viz.csv')
path = download(url, data_path, progressbar=True, verbose=True)

# Dataframe creation, keeping only useful columns
df = pd.read_csv(data_path, sep=";", usecols=[0, 7, 8, 13])

# Dropping duplicates, renaming for convenience
df.drop_duplicates(inplace=True)
df = df.rename(columns={"code_commune": "code", "nom_commune": "nom",
                        "consommation_annuelle_moyenne_de_la_commune_mwh": "conso"})
# Dept for each city, delete last 3 digits of the code
df['dept'] = df['code'].apply(lambda x: int(str(x)[:-3]))
# Only one NaN, replacing with the appropriate city name, Florange
df.fillna('Florange', inplace=True)
# Converting city names to lower case to avoid case errors
df['nom'] = df['nom'].str.lower()


# TODO fix path names with os
city = '../../data/communes.geojson'
dept = '../../data/departements.geojson'
region = '../../data/regions.geojson'

cities = json.load(open(city, 'r'))

# Plots
# TODO Violin plot per city
# TODO define a class to get max min per region, dept


def max_conso(dept, year=2018):
    """Get the city with maximum consumption on the given year
    and return city, conso"""
    dept_df = df[df['annee'] == year and df['dept'] == dept]
    conso = 0
    town = 0
    return town, conso


def min_conso(dept, year=2018):
    """Get the city with maximum consumption on the given year
    and return city, conso"""
    dept_df = df[df['annee'] == year and df['dept'] == dept]
    conso = 0
    town = 0
    return town, conso


class City:
    def __init__(self, id):
        """Constructor of City objects.
        code -- code of the city (recommended), can also be the name of the city in lowercase"""
        self.id = id

    def kde(self):
        """Plots the kde of the city over the available years"""
        if type(self.id) == int:
            kde_df = df[df['code'] == self.id]
        if type(self.id) == str:
            kde_df = df[df['nom'] == self.id]
        fig = sns.kdeplot(data=kde_df, x='conso', fill=True)
        return fig

    def swarm(self):
        """Plots the swarm plot of the city over the available years"""
        if type(self.id) == int:
            swarm_df = df[df['code'] == self.id]
        if type(self.id) == str:
            swarm_df = df[df['nom'] == self.id]
        fig = sns.swarmplot(data=swarm_df, x='conso')
        return fig

    def violin(self):
        """Plots the violin plot of the city over the available years"""
        if type(self.id) == int:
            violin_df = df[df['code'] == self.id]
        if type(self.id) == str:
            violin_df = df[df['nom'] == self.id]
        fig = sns.violinplot(data=violin_df, x='conso')
        return fig

    def bar(self):
        """Plots the bar plot of the city over the available years"""
        if type(self.id) == int:
            bar_df = df[df['code'] == self.id]
        if type(self.id) == str:
            bar_df = df[df['nom'] == self.id]
        fig = sns.barplot(data=bar_df, x='annee', y='conso')
        return fig

    def show(self):
        """Displays the plot"""
        # TODO
        pass


# Interactive map
# App layout
app = Dash(__name__)

app.layout = html.Div([

    html.H1("French electricity consumption", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2018", "value": 2018},
                     {"label": "2019", "value": 2019},
                     {"label": "2020", "value": 2020},
                     {"label": "2021", "value": 2021}],
                 multi=False,
                 value=2018,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='elec_map', figure={})

])


# Connect plotly to Dash
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='elec_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by the user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["annee"] == option_slctd]

    fig = px.choropleth_mapbox(dff,
                               geojson=cities,
                               color="conso",
                               locations="code",
                               featureidkey="properties.code",
                               mapbox_style="carto-positron",
                               hover_data=['conso'],
                               zoom=3.7,
                               center={"lat": 47, "lon": 2},
                               opacity=0.6,
                               )

    return container, fig


if __name__ == '__main__':
    app.run_server(debug=True)
