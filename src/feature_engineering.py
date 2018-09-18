from bb_data import get_labeled_raw_data
from raw_dex_reader import get_species_from_dex
import json

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
    labelled_data[well] = get_labeled_raw_data(r"../data/" + well + "_BIOSTRAT_RAW_1.DEX", r"../data/" + well + "_BIOSTRAT_COMPUTED_1.DEX")
    species_dictionaries[well] = get_species_from_dex(r"../data/" + well + "_BIOSTRAT_RAW_1.DEX")

master_dict = almalgamate_species_dictionaries(species_dictionaries)

with open("../data/json/master_dict.json", "w") as f:
    f.write(json.dumps(master_dict))

for well in wells:
    with open("../data/json/" + well + "_labelled.json", "w") as f:
        f.write(labelled_data[well].to_json())
