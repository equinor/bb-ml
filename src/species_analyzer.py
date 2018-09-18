from typing import List
from raw_dex_reader import get_species_from_dex
import editdistance


class SpeciesAnalyzer:
    def __init__(self, species: dict):
        self._species = species

    def _pairwise(self, iterable):
        a = iter(iterable)
        return zip(a, a)

    def find_duplicate_species(self):
        new_dict = {}
        for key, value in self._species.items():
            new_dict.setdefault(value, set()).add(key)
        return [{key: values} for key, values in new_dict.items() if len(values) > 1]

    def edit_distance_duplicates(self, max_edit_distance=3):
        s = self._species
        return [{a: s[a], b:s[b]} for a, b in self._pairwise(self._species) if editdistance.eval(s[a], s[b]) < max_edit_distance]


def run(filenames: List[str]):
    all_species = {}
    all_duplicates = []
    for filename in filenames:
        species = get_species_from_dex(filename)
        analyzer = SpeciesAnalyzer(species)

        print(str.format("Edit distance matches: {}", analyzer.edit_distance_duplicates()))
        all_duplicates.extend(analyzer.find_duplicate_species())
        all_species = {**all_species, ** species}
    all_analyzer = SpeciesAnalyzer(all_species)
    all_analyzer.find_duplicate_species()
    
    print(str.format("Exact matches: {}", all_duplicates))


if __name__ == "__main__":
    import glob
    pathnames = glob.glob("..\\data\\*RAW*.DEX")
    print(pathnames)
    run(pathnames)
