.. Moyenne_sources documentation master file, created by
sphinx-quickstart on Tue Nov 22 11:38:04 2022.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive.

Documentation de TRACKELEC
======================================================================

.. image:: https://www.entraid.com/wp-content/uploads/2017/09/tracteur-electrique-john-deere-sesam-essais.jpg
   :height: 250
   :width: 400
   :scale: 100
   :align: center
   :alt: tracteur éléectrique John Deere Sesam

Présentation
=============

Cette page a pour but d'héberger la documentation de notre projet nommé TRACKELEC.

TRACKELEC a pour objectif de prédire la consommation d'électricité au jour du 8 décembre 2022 et de fournir une carte intéractive de la France présentant la consommation annuelle moyenne d'électricité entre 2018 et 2021.

Ce projet est divisé en deux parties:
    - une partie prédiction
    - une partie visualisation 


Procédure d'installation
=========================
Pour utiliser notre projet, téléchargez le dossier https://github.com/mle-seach/hax712x_project/ .
Puis veillez à télécharger les modules donnés dans le fichier ``requirements.txt`` grâce à la commande ``pip``.




   
   
Partie Prédiction
==================

Dans un premier temps, nous avons réalisé la prédiction globale de la consommation d'électricité au jour du 8 décembre 2022.
Nous nous sommes basés sur le module ``prophet``, vous pouvez retrouver la documentation de cette partie dans l'onglet Prédiction de la consommation d'électricité en France avec Prophet.

Dans un second temps, nous avons différencié les sources d'énergie produisant l'électricité afin d'estimer leur utilisation à ce même jour.
Les codes correspondant à cette partie ce nomment ``moyenne_autres_sources.py`` et ``pred_sources.py``, vous pouvez retrouver respectivement leur documentation dans les parties 
Moyenne des sources d'éléctricité et Prédiction des sources d'électricité. 

Partie Visualisation 
====================

Cette partie, nous avons réalisé la visualisation des consommations annuelles moyennes d'électricité entre 2018 et 2021;
Le code correspondant à cette partie ce nomme ``ggg``, vous pouvez retrouver sa documentation dans la partie 


.. toctree::
   :maxdepth: 1
   :caption: Table des matières:


   ./moysources.rst
   ./predsources.rst
   ./prophetpred.rst 

Indices and tables
==================

* :ref:`modindex`
* :ref:`search`
