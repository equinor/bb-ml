import pandas as pd


input_dex = "C:\\Users\\dawad\\FORCE\\bb-ml\\data\\15_9-F-1 A_BIOSTRAT_RAW_1.DEX"

with open(input_dex) as f:
    raw_file = f.read()

species_list = raw_file.split("[SPECIES LIST]")[1].split("[END OF FILE]")[0].split("\n")[1:]

#species_list = species_list[0:12]
print(species_list)

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

print(species_dict)

samples_list = raw_file.split("[SPECIES LIST]")[0].split("[SAMPLE ")[1:]

print(len(samples_list))

sample_data = {}

for sample in samples_list:
    depth = float(sample.split('m')[0])
    sample_id = sample.split("Sample id = ")[1].split("\n")[0]
    print(sample_id, depth)
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
    sample_data[sample_id] = depth, counts_dict

print(sample_data)

print(len(sample_data))


df = pd.DataFrame(0, columns=species_dict.keys(), index=sample_data.keys())
df["Depth"] = None

print(df)

for sample_id, sample in sample_data.items():
    depth, counts_dict = sample
    df.at[sample_id, 'Depth'] = depth
    for key, val in counts_dict.items():
        df.at[sample_id, key] = val

print(df)




