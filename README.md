# HAX712X Project TRACKELEC

<p align="center">
  <img src="https://github.com/mle-seach/hax712x_project/blob/master/data/tracteur_electrique.jpg" width=400 title="Tracteur">
</p>


##  Introduction

Bienvenue sur le github de notre projet nommé TRACKELEC.

Ce  projet Python possède deux buts principaux :

-Dans un premier temps, l'objectif est de prédire la consommation d'électricité en France le 08/12/2022. Il faudra également fournir des graphiques représentant les prédictions des différentes sources électriques telles que le gaz, le vent etc...

-Dans un second temps, notre mission est de créer une carte intéractive fournissant la consommation annuelle moyenne d'électricite des français entre 2018 et 2021 afin de mieux comprendre les dépenses électriques en France. 

## Histoire du nom du projet

Le nom de notre projet provient des mots tracteur et électricité. 
En effet, depuis quelques années maintenant l'utilisation de voitures électriques s'est démocratisée en France ce qui a chamboulé la consommation en électricité des français par rapport aux débuts des années 2000. Cependant la grande révolution des engins électriques reste le développement de tracteurs électriques pour travailler dans les champs. 

Nous avons donc choisi d'associer le mot électricité (qui est le coeur de notre projet) avec le mot tracteur (qui représente l'innovation dans le mode électrique). 

Vous pouvez également constater que trackelec contient un autre jeu de mot, trackelec peut se voir comme track-elec, soit suivre l'électricité, ce qui est le but de notre projet.

# Préparation de l'environnement de travail :

Une partie de ce projet a été effectuée sur Jupyter Notebook , avant de pouvoir expérimenter notre code , vous devez d'abord vous assurer d'avoir un environnement de travail fonctionnel (si cela est déja fait vous pouvez passer à la deuxième étape).

## Première étape : 

 - Installez `Anaconda` en suivant les instructions sur le lien : <https://www.anaconda.com/products/distribution> .
 
 - Lancez `Jupyter Notebook` après avoir lancé `Anaconda` en cliquant sur l'icône "launch" .
 
 Si vous avez des difficultés nous vous invitions à consulter le cours [IntroPython.pdf](http://josephsalmon.eu/enseignement/Montpellier/HLMA310/IntroPython.pdf).

## Deuxième étape : 

- Clônez le référentiel et accédez au dossier prédiction :

```bash 
git clone https://github.com/mle-seach/hax712x_project.git 
cd hax712x_project/project/prediction/
```

- Créez un nouvel environnement de travail nommé "trackelec_env":

```bash
conda create -n trackelec_env python=3.9.12
```
- Après avoir basculé dans votre nouvel environnement python, téléchargez les modules présents dans le fichier requirements.txt via une commande `pip` suivante:

```bash
pip install -r requirements.txt 
``` 
- Après avoir effectué toutes ces manipulations , vous pouvez enfin installer notre module `trackelec` via la commande suivante :

```bash
pip install -i https://test.pypi.org/simple/ trackelec
``` 

# Les données 

Pour ce projet nous avons utilisé plusieurs jeux de données.

- Pour la partie prédiction, vous pouvez retrouver les jeux de données aux adresses suivantes : https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B et  https://odre.opendatasoft.com/explore/dataset/eco2mix-national-tr/information/?disjunctive.nature&sort=-date_heure .

- Pour la partie visualisation, vous pouvez retrouver le jeux de données à l'adresse suivante :  https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/information/ . 

Toutes ces données ont été manipulées avec la bibliothèque ```pandas``` présente sur Python afin de les nettoyer et d'en extraire seulement les informations nécessaires à notre travail.


# Prédiction :

Comme présenté lors dans l'introduction, cette partie a pour but de prédire la consommation d'électricité en France au jour du 08/12/2022.
Nous avons fait le choix d'utiliser deux méthodes différentes de prédiction afin de pouvoir les comparer. 

Pour la consommation d'électricité globale, nous avons utilisé le module ```prophet``` présent dans Python qui effectue des prévisions de séries temporelles basées sur un modèle additif .

Pour la consommation des différentes sources d'énergie, nous avons utilisé la méthode de la moyenne empirique et la méthode Prophet. 


# Projet Mid-term :

## Programme de travail et affectation des tâches 
Afin de répartir au mieux le travail, nous avons fait le choix de ''créer deux équipes'' : Mathieu et Thibault qui se chargeront de la partie carte intéractive et analyse  la consommation française d'électricite, et Sarah et Pauline qui se chargeront de la partie prédiction  du 8 décembre. 
Nous avons également Guillaume à qui nous avons attribué le rôle de consultant, car de part son travail il ne peut pas s'investir réellement dans le projet.
Bien évidemment, ces deux parties du projet étant liées, certains éléments utilisés dans une partie seront probablement utilisés dans une autre : chaque membre du groupe apportera sa pierre à l'édifice.

Dans la partie prédiction, Sarah et Pauline travaillent en collaboration cependant, Sarah se charge plus de la partie sur l'électricité en généralité et Pauline étudie plus les autres sources d'énergie.

## Contact:

Pauline Dusfour-Castan : pauline.dusfourcastan@gmail.com


Thibault Ferretti : thibault.ferretti@etu.umontpellier.fr


Sarah Matoub : sarah19mtb@gmail.com


Mathieu Le-Seach : mathieu.le-seach@etu.umontpellier.fr


Guillaume Bernard-Reymond : guillaume.bernardreymond@gmail.com
