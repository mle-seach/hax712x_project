import os
import pandas as pd
from download import download
from trackelec.io import url_dataviz, path_target


class load_dataviz:
    def __init__(self, url=url_dataviz, target_name=path_target):
        download(url, target_name, progressbar=True)

    @staticmethod
    def save_as_df():
        df_elec = pd.read_csv(path_target, sep=";", usecols=[0, 7, 8, 13])
        return df_elec