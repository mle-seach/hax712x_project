import os

from download import download
import pandas as pd
import plotly.express as px
import json
from flask_caching import Cache
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
# Adding 0 at the start of the city code if in one of the first 9 dept
df['code'] = df['code'].apply(lambda id: str(id) if id > 9999 else "0" + str(id))
# Dept for each city, delete last 3 digits of the code
df['dept'] = df['code'].apply(lambda x: int(str(x)[:-3]))
# Only one NaN, replacing with the appropriate city name, Florange
df.fillna('Florange', inplace=True)
# Converting city names to lower case to avoid case errors
df['nom'] = df['nom'].str.lower()

# TODO fix geojson paths
city_path = '../../data/communes2.json'
dept_path = '../../data/dept.geojson'
cities = json.load(open(city_path, 'r'))

# TODO map by dept


# Plots and max/min
def max_conso(dept, year=2018):
    """Get the city with maximum consumption of the dept on the given year
    and return city name and its conso"""
    temp_df = df[df['annee'] == year]
    temp_df = temp_df[temp_df['dept'] == dept]
    row = temp_df[temp_df['conso'] == temp_df['conso'].max()]

    return row.iloc[0]['nom'], row.iloc[0]['conso']


def min_conso(dept, year=2018):
    """Get the city with minimum consumption of the dept on the given year
    and return city, conso"""
    temp_df = df[df['annee'] == year]
    temp_df = temp_df[temp_df['dept'] == dept]
    row = temp_df[temp_df['conso'] == temp_df['conso'].min()]

    return row.iloc[0]['nom'], row.iloc[0]['conso']


class City:
    def __init__(self, id):
        """Constructor of City objects.
        id -- code of the city"""
        self.id = id

    def swarm(self):
        """Plots the swarm plot of the city over the available years"""
        temp_df = df[df['code'] == self.id]
        fig = px.strip(temp_df, x='conso', labels={'conso': f'Consumption of city: {self.id}'})
        return fig

    def violin(self):
        """Plots the violin plot of the city over the available years"""
        temp_df = df[df['code'] == self.id]
        fig = px.violin(temp_df, x='conso', labels={'conso': f'Consumption of city: {self.id}'})
        return fig

    def bar(self):
        """Plots the bar plot of the city over the available years"""
        temp_df = df[df['code'] == self.id]
        fig = px.bar(temp_df, x='annee', y='conso', labels={'conso': f'Consumption of city: {self.id}'})
        return fig


def hist(dept):
    temp_df = df[df['dept'] == dept]
    fig = px.bar(temp_df, x='nom', y='conso').update_xaxes(categoryorder="total descending")
    return fig


# Interactive map

app = Dash(__name__)

cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})
CACHE_TIMEOUT = int(os.environ.get('DASH_CACHE_TIMEOUT', '60'))


@cache.memoize(timeout=CACHE_TIMEOUT)
def compute_map_data():
    dff = df.copy()
    dff = dff.groupby(['code', 'dept']).agg({'conso': 'mean', 'nom': 'first'}).reset_index()

    return dff


# App layout
app.layout = html.Div([
    html.H1("French electricity consumption", style={'text-align': 'center'}),
    # Control Panel
    html.Div([
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

        dcc.Dropdown(id="slct_plot_style",
                     options=[
                         {"label": "Violin", "value": 'violin'},
                         # {"label": "KDE", "value": 'kde'},
                         {"label": "Swarm", "value": 'swarm'},
                         {"label": "Bar", "value": 'bar'}],
                     multi=False,
                     value='violin',
                     style={'width': "40%"}
                     ),
        html.Br(),

        # Visuals
        html.Div(className="row", children=[
            html.Div(className="seven columns pretty_container", children=[
                dcc.Markdown(children='_Click on the map to show the city\'s consumption._'),
                dcc.Graph(id='elec_map', clickData={'points': [{'customdata': '34172'}]})
            ]),
            html.Div(className="row2", children=[
                dcc.Graph(id='plot'),
            ]),
        ]),
    ]),
])


# Connect plotly to Dash
@app.callback(
    Output(component_id='elec_map', component_property='figure'),
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)

    dff = compute_map_data()

    fig = px.choropleth_mapbox(dff,
                               geojson=cities,
                               color="conso",
                               locations="code",
                               featureidkey="properties.code",
                               mapbox_style="carto-positron",
                               hover_data=['conso'],
                               zoom=4,
                               center={"lat": 47, "lon": 2},
                               opacity=0.6,
                               )

    hovertemplate = '<br>City code: %{location}' \
                    '<br>Conso: %{customdata:.3s} MWh/hb'
    fig.data[0]['hovertemplate'] = hovertemplate

    return fig


@app.callback(
    Output(component_id='plot', component_property='figure'),
    [Input(component_id='slct_plot_style', component_property='value'),
     Input(component_id='elec_map', component_property='clickData')]
)
def update_plot(option_slctd, clickdata):
    print(option_slctd, clickdata['points'][0]['location'])

    code = clickdata['points'][0]['location']
    print(type(code), code)

    if option_slctd == 'violin':
        fig2 = City(code).violin()
    if option_slctd == 'swarm':
        fig2 = City(code).swarm()
    if option_slctd == 'bar':
        fig2 = City(code).bar()

    return fig2


if __name__ == '__main__':
    app.run_server(debug=True)
