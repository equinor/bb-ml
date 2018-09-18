
# input_dex = "C:\\Users\\dawad\\FORCE\\bb-ml\\data\\15_9-F-1 A_BIOSTRAT_RAW_1.DEX"
def read_raw_dex(input_dex):
    with open(input_dex) as f:
        raw_file = f.read()

    species_list = raw_file.split("[SPECIES LIST]")[1].split("[END OF FILE]")[0].split("\n")[1:]

    #species_list = species_list[0:12]
    # print(species_list)

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
# print(species_dict)