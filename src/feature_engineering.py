from bb_data import get_labeled_raw_data
from raw_dex_reader import get_species_from_dex
import pandas as pd
import numpy as np
from sklearn import preprocessing

def almalgamate_species_dictionaries(species_dictionaries):
    master_dict = {}
    for well in species_dictionaries:
        for key, val in species_dictionaries[well].items():
            master_dict[key] = val
    return master_dict

wells = ["15_9-F-1 A", "15_9-F-1 B", "15_9-F-1", "15_9-F-11 A", "15_9-F-11 B"]

labelled_data = {}
species_dictionaries = {}

for well in wells:
    labelled_data[well] = get_labeled_raw_data(r"../data/" + well + "_BIOSTRAT_RAW_1.DEX", r"../data/" + well + "_BIOSTRAT_COMPUTED_1.DEX", well)
    species_dictionaries[well] = get_species_from_dex(r"../data/" + well + "_BIOSTRAT_RAW_1.DEX")

master_dict = almalgamate_species_dictionaries(species_dictionaries)

print(len(master_dict))




for well_id in wells:
    labelled_data[well_id] = labelled_data[well_id].sort_values("Depth")
    for column in labelled_data[well_id]:
        if column not in ["Depth", "label", "Well_name"]:
            labelled_data[well_id][column] = pd.to_numeric(labelled_data[well_id][column])
#            cumsum = labelled_data[well_id][column].cumsum()
#            cumsum = cumsum.divide(cumsum.max())
#            labelled_data[well_id][column + "_cumsum"] = cumsum
#            norm = labelled_data[well_id][column]
#            norm = norm.divide(norm.sum())
#            labelled_data[well_id][column + "_norm"] = norm



list = [df for df in labelled_data.values()]

label_raw_data = pd.concat(list, sort=True)
label_raw_data = label_raw_data.replace(np.nan, 0)

label_raw_data.to_csv("../data/output/test.csv")