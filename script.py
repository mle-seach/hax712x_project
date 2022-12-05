import trackelec as track

df_viz = track.load_dataviz().save_as_df()
df_cons = track.load_datacons().save_as_df()
df_cons2022 = track.load_datacons2022().save_as_df()
