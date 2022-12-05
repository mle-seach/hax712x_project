import os

url_dataviz = "https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/download"
path_target = os.path.join(os.getcwd(), "trackelec", "visu", "data_viz.csv")

url_datacons = "https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
path_conso = os.path.join(os.getcwd(), "trackelec", "predic",
                          "consommation3.csv")

url_datacons2022 = "https://odre.opendatasoft.com/explore/dataset/eco2mix-national-tr/download/?format=csv&disjunctive.nature=true&q=date_heure:%5B2022-05-31T22:00:00Z+TO+2022-11-29T22:59:59Z%5D&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
path_conso2022 = os.path.join(os.getcwd(), "trackelec", "predic",
                              "consommation_2022.csv")
