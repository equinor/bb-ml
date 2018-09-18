from typing import List
from raw_dex_reader import read_raw_dex


class SpeciesAnalyzer:
    def __init__(self, species: dict):
        self._species = species

    def find_duplicate_species(self):
        new_dict = {}
        for key, value in self._species.items():
            new_dict.setdefault(value, set()).add(key)
        return [{key: values} for key, values in new_dict.items() if len(values) > 1]


def run(filenames: List[str]):
    all_species = {}
    all_duplicates = []
    for filename in filenames:
        species = read_raw_dex(filename)
        analyzer = SpeciesAnalyzer(species)
        all_duplicates.extend(analyzer.find_duplicate_species())
        all_species = {**all_species, ** species}
    analyzer = SpeciesAnalyzer(all_species)
    analyzer.find_duplicate_species()
    print(all_duplicates)


if __name__ == "__main__":
    import glob
    pathnames = glob.glob("..\\data\\*RAW*.DEX")
    print(pathnames)
    run(pathnames)
