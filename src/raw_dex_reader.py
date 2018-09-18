import pandas as pd
import os

def get_species_from_dex(input_dex):
    with open(input_dex) as f:
        raw_file = f.read()

    species_list = raw_file.split("[SPECIES LIST]")[1].split("[END OF FILE]")[0].split("\n")[1:]

    species = None
    id = None

    species_dict = {}

    for line in species_list:
        if species is not None and id is not None:
            species_dict[id] = species
            species = None
            id = None
        if line.find("Species") == 0:
            species = line[10:]
        if line.find("  ID : ") > 0:
            id = line[8:]
    return species_dict


def get_dex_as_dataframe(input_dex):
    species_dict = get_species_from_dex(input_dex)

    with open(input_dex) as f:
        raw_file = f.read()

    samples_list = raw_file.split("[SPECIES LIST]")[0].split("[SAMPLE ")[1:]

    sample_data = {}

    for sample in samples_list:
        depth = float(sample.split('m')[0])
        sample_id = sample.split("Sample id = ")[1].split("\n")[0]
        counts_dict = {}
        for species_data in sample.split("Species = "):
            if species_data.find("Species id : ") > 0:
                species_id = species_data.split("Species id : ")[1].split("\n")[0]
                count = 0
                if species_data.find("Species count : ") > 0:
                    count = int(species_data.split("Species count : ")[1].split("\n")[0])
                if species_data.find("Abundance : +") > 0:
                    count = 50
                counts_dict[species_id] = count
        sample_data[int(sample_id)] = depth, counts_dict

    df = pd.DataFrame(0, columns=species_dict.keys(), index=sample_data.keys())
    df["Depth"] = None

    for sample_id, sample in sample_data.items():
        depth, counts_dict = sample
        df.at[sample_id, 'Depth'] = depth
        for key, val in counts_dict.items():
            df.at[sample_id, key] = val
    return df


if __name__ == "__main__":
    root = "C:\\Users\\dawad\\FORCE\\bb-ml\\data\\"
    wells = ["15_9-F-1", "15_9-F-1 A", "15_9-F-1 B", "15_9-F-4", "15_9-F-11 A", "15_9-F-11 B"]
    # 15_9-F-10 #This one is a bit different! Only one species
    suffix = "_BIOSTRAT_RAW_1.DEX"

    for well in wells:
        input_dex = os.path.join(root, well + suffix)
        df = get_dex_as_dataframe(input_dex)
        with open(os.path.join(root, "json", well + "_raw.json"), "w") as f:
            f.write(df.to_json())
