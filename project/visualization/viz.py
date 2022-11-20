import os

from download import download
import pandas as pd
import plotly.express as px
import json
from dash import Dash, dcc, html, Input, Output

pd.set_option('display.max_columns', None)

# Data cleaning
# TODO look for missing data, separate per year

url = 'https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/download'
data_path = os.path.join(os.getcwd(), 'data_viz.csv')
path = download(url, data_path, progressbar=True, verbose=True)

df = pd.read_csv(data_path, sep=";")
# Keeping useful columns, dropping duplicates, renaming for convenience
df = df.loc[:, df.columns.intersection(['annee', 'code_commune', 'nom_commune',
                                        'consommation_annuelle_moyenne_de_la_commune_mwh'])]
df.drop_duplicates(inplace=True)
df = df.rename(columns={"code_commune": "code", "nom_commune": "nom",
                        "consommation_annuelle_moyenne_de_la_commune_mwh": "conso"})



city = '../../data/communes.geojson'
dept = '../../data/departements.geojson'
region = '../../data/regions.geojson'


cities = json.load(open(city, 'r'))
for feature in cities['features']:
    feature["code_commune"] = feature["properties"]["code"]

# Plots
# TODO Violin plot per year per city

# Interactive map
# TODO define a class to get max min per region, dept


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

    fig = px.choropleth_mapbox(dff.head(20),
                               geojson=cities,
                               color="conso",
                               locations="code",
                               featureidkey="properties.code",
                               mapbox_style="carto-positron",
                               hover_data=['conso'],
                               zoom=4,
                               center={"lat": 46, "lon": 2},
                               opacity=0.6,
                               )

    return container, fig


if __name__ == '__main__':
    app.run_server(debug=True)
