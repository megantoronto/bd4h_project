import numpy as np
import pandas as pd
import os
import re

data_loc = "data/length-of-stay/test"
out_loc = "data/length-of-stay/test_upd"

# names_file = pd.read_csv("data_filenames.csv")
names_file = pd.read_csv("testdata_filenames.csv")

names_file


train_files = os.listdir(data_loc)
train_files = [f for f in train_files if re.search("episode", f)]
train_files
for i in train_files:
    episode_data = pd.read_csv(os.path.join(data_loc, i))
    episode_data["X"] = np.nan
    episode_data["Y"] = ""

    episode_data.at[0, "X"] = names_file[names_file["filename"].values == i].iloc[0]["X"]
    episode_data.at[0, "Y"] = names_file[names_file["filename"].values == i].iloc[0]["Y"]

    episode_data.to_csv(os.path.join(out_loc, i), index=False)
