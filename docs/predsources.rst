Prédiction des sources d'électricité 
=====================================

Dans cette partie, nous allons faire la documentation du code ``pred_sources.py``.

But du code
------------

Ce code a pour but de prédire la consommation électrique produite par différentes sources d'énergie au jour du 8 décembre 2022.

Explication du code en généralité
-----------------------------------

Dans un pemier temps, il nous faut importer les données présentes au lien suivant : https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B .
Après ça, nous avons choisi la colonne 'Date' comme index afin de récupérer seulement les données du 8 décembre de chaque année disponible.
*En effet, nous avons fait le choix de faire notre prédiction selon l'estimateur de l'espérance. Il nous faut donc calculer la moyenne empirique.*

Nous avons par la suite créé des 'sous-data' qui contiendront chacun les données des différentes sources d'énergie et les heures.
Nous avons fait le choix de placer, l'éolien, l'hydraulique et le solaire dans le même dataframe car ce sont toutes des sources d'énergie dites renouvelables/propres.

Dans chaque cas, nous avons nettoyé notre jeu de données avec la commande ``data.dropna()`` et trié les valeurs selon l'axe Heure.
Nous avons ensuite calculer la moyenne empirique de chaque source en fonction des heures.

Pour finir, nous avons réalisé un plot simple afin d'afficher nos résultats sous forme de graphiques. 

Dans une deuxième partie du code, nous avons souhaité réaliser une autre prédiction selon le module Prophet et comparer les résultats obtenus avec ceux de la première méthode.
La documentation de ce module se trouve à l'adresse suivante : https://facebook.github.io/prophet/docs/quick_start.html . 

Documentation de quelques commandes :
--------------------------------------

.. code:: python

    pd.read_csv()

permet de lire un fichier csv et de le mettre sous forme de dataframe

.. code:: python

    dataframe.set_index()

permet de ré-indéxer le dataframe selon une colonne choisie

.. code:: python

    dataframe.loc()

permert de récupérer certaines lignes d'un dataframe selon l'index 

.. code:: python

    dataframe.dropna()

permet de nettoyer le jeu de données

.. code:: python

    dataframe.sort_values()

permet de trier les valeurs selon un axe

.. code:: python

    dataframe.groupby()[].mean

permet de calculer la moyenne de la colonne entre crochets selon la colonne entre parenthèses


Pour plus d'informations sur ces différentes fonctions et leur utilisation vous pouvez consulter le lien suivant : https://pandas.pydata.org/docs/user_guide/index.html .

