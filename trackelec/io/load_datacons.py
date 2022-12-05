import pandas as pd
from download import download

from trackelec.io import url_datacons, path_conso


class load_datacons:
    def __init__(self, url=url_datacons, target_name=path_conso):
        download(url, target_name, progressbar=True)

    @staticmethod
    def save_as_df():
        df_elec = pd.read_csv(path_conso, sep=";")
        return df_elec
