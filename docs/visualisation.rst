Visualisation de la consommation électrique en France :
===================================================================

Objectif de cette section : Visualisation de la consommation électrique française au niveau des villes/départements.


Introduction : 
-----------------------------------------------------------------

La partie Visualisation a été construite en deux parties :

Une carte par départements avec un histogramme des différentes consommations par villes en fonction du département.

Une carte par villes avec la distribution des différentes valeurs de consommation au cours des quatre années données.


1. Carte par départements et histogramme:
---------------------------------------------------------------------
Pour la construction de la carte on a utilisé un fichier geojson que l'on a relié aux données de consommation électriques.

.. _url1: https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements.geojson

Création de la carte par départements :

 .. image:: Images/dept.png 
    :scale: 50%
    :align: center

.. code:: python

    elec_map_fig = px.choropleth_mapbox(
        df2,
        geojson=dept,
        color=df2.conso,
        locations=df2.nom,
        featureidkey="properties.nom",
        hover_data=["conso"],
        center={"lat": 47, "lon": 2},
        mapbox_style="carto-positron",
        zoom=4.8,
    )

Pour l'histogramme on a construit deux menus déroulants, un pour choisir la région et un autre pour choisir le département.
Ces deux menus déroulants étant liées on a du construire des fonctions utilisant des "callback" pour permettre un choix dynamique.

Histogramme:

 .. image:: Images/hist.png 
    :scale: 50%
    :align: center

.. code:: python

    def hist(dept):
    """Histogram of the cities' consumption in the dept or region"""
    # Region
    dff = compute_map_data()
    temp_df = dff[dff["dept"] == dept]
    fig = px.bar(temp_df, x="nom", y="conso").update_xaxes(
        categoryorder="total descending"
    )
    return fig


Menus déroulants : 

.. code:: python 

    # Dropdown of regions
    @app.callback(Output("slct_dept", "options"), Input("slct_reg", "value"))
    def set_dept_options(selected_region):
        return [{"label": label(i), "value": i} for i in regions[selected_region]]


    # Dropdown of depts
    @app.callback(Output("slct_dept", "value"), Input("slct_dept", "options"))
    def set_dept_value(available_options):
        return available_options[0]["value"]
    
2. Carte par villes : 
--------------------------------------------------------------------------------
Pour la carte par villes on aussi utilisé un fichier geojson disponible ici:

.. _url2: = https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/communes.geojson


Création de la carte par villes :

 .. image:: Images/communes.png 
    :scale: 50%
    :align: center

.. code:: python

    def update_graph():
        print()

        dff = compute_map_data()

        fig = px.choropleth_mapbox(
            dff,
            geojson=cities,
            color="conso",
            locations="code",
            featureidkey="properties.code",
            mapbox_style="carto-positron",
            hover_data=["conso", "nom"],
            zoom=4,
            center={"lat": 47, "lon": 2},
            opacity=0.6,
        )

        return fig



En cliquant sur la carte on peut sélectionner la ville que l'on veut et ensuite afficher la distribution voulue des différentes consommations au cours des quatres années données.

 .. image:: Images/violin.png 
    :scale: 50%
    :align: center

.. code:: python 

    def update_plot(option_slctd, clickdata):
        print(option_slctd, clickdata["points"][0]["location"])

        code = clickdata["points"][0]["location"]
        print(type(code), code)

        if option_slctd == "violin":
            fig2 = City(code).violin()
        elif option_slctd == "swarm":
            fig2 = City(code).swarm()
        elif option_slctd == "bar":
            fig2 = City(code).bar()

        return fig2