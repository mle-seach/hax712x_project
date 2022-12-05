import pandas as pd
from download import download

from trackelec.io import url_datacons2022, path_conso2022


class load_datacons2022:
    def __init__(self, url=url_datacons2022, target_name=path_conso2022):
        download(url, target_name, progressbar=True)

    @staticmethod
    def save_as_df():
        df_elec = pd.read_csv(path_conso2022, delimiter=";",
                              comment="#",
                              na_values="n/d",
                              parse_dates=["Date"],
                              converters={"heure": str}, )
        return df_elec
