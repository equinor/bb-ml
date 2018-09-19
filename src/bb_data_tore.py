import pandas as pd
import numpy as np
from parse_computed import get_interval_df
from raw_dex_reader import get_dex_as_dataframe as get_dex_as_dataframe2

def get_dex_as_dataframe(fn, well_name):
    raw = get_dex_as_dataframe2(fn)
    raw["Well_name"] = well_name
    return raw

def transform_labels_to_ages(label):
    transform_dictionary = {
     'Barremian or older':125,
     'Barremian? or older':125,
     'E Tithonian':145,
     'Early-Late Tithonian':145,
     'Late Tithonian':145,
     'E?-M Oxfordian?':160,
     'Early-Mid Oxfordian':160,
     'Early?-Mid Oxfordian':160,
     'Mid Oxfordian':160,
     'M-L Oxf':160,
     'L Oxfordian':160,
     'Early Berriasian':145,
     'Early Maastrichtian':72,
     'Indeterminate -possibly Triassic':230,
     'Late Callovian':165,
     'Mid Callovian':165,
     'Mid-Late Callovian':165,
     'Mid-Late Callovian or older':165,
     'Late Callovian-Early Oxfordian':165,
     'Late Coniacian? - Early Santonian':86,
     'Late Paleocene':66
     }
    if label in transform_dictionary.keys():
        return transform_dictionary[label]
    else:
        return None

def get_labeled_raw_data(fn_raw_data, fn_computed_data, well_name):
    raw = get_dex_as_dataframe(fn_raw_data, well_name)
    
    computed_interval = get_interval_df(fn_computed_data)
    
    chronostratigraphic_df = computed_interval[computed_interval["Type"]=="Chronostratigraphy"].copy()
    
    chronostratigraphic_df["Top_sample_ID"] = chronostratigraphic_df["Top_sample_ID"].apply(pd.to_numeric)
    chronostratigraphic_df["Base_sample_ID"] = chronostratigraphic_df["Base_sample_ID"].apply(pd.to_numeric)
    
    def get_label(chronostratigraphic_df, index):
        mask = (chronostratigraphic_df["Top_sample_ID"] <= index ) & (chronostratigraphic_df["Base_sample_ID"] >= index )
        try:
            value = chronostratigraphic_df[mask]["name"].values[0]
        except:
            value = np.nan
        return value
    
    raw["label"] = raw.index.map(lambda x: get_label(chronostratigraphic_df, int(x)))
    raw["age"] = raw["label"].map(transform_labels_to_ages)
    labeled_samples = raw.dropna()
    return labeled_samples

test1 = get_labeled_raw_data(r"../data/15_9-F-1 A_BIOSTRAT_RAW_1.DEX", r"../data/15_9-F-1 A_BIOSTRAT_COMPUTED_1.DEX", "15_9-F-1 A")
test2 = get_labeled_raw_data(r"../data/15_9-F-1 B_BIOSTRAT_RAW_1.DEX", r"../data/15_9-F-1 B_BIOSTRAT_COMPUTED_1.DEX", "15_9-F-1 B")
test3 = get_labeled_raw_data(r"../data/15_9-F-1_BIOSTRAT_RAW_1.DEX", r"../data/15_9-F-1_BIOSTRAT_COMPUTED_1.DEX", "15_9-F-1")
test4 = get_labeled_raw_data(r"../data/15_9-F-11 A_BIOSTRAT_RAW_1.DEX", r"../data/15_9-F-11 A_BIOSTRAT_COMPUTED_1.DEX", "15_9-F-11 A")
test5 = get_labeled_raw_data(r"../data/15_9-F-11 B_BIOSTRAT_RAW_1.DEX", r"../data/15_9-F-11 B_BIOSTRAT_COMPUTED_1.DEX", "15_9-F-11 B")
labeled_raw_data = pd.concat([test1, test2,test3,test4,test5], sort=True)
labeled_raw_data=labeled_raw_data.replace(np.nan, 0)
labeled_raw_data.index = labeled_raw_data["Well_name"]+labeled_raw_data.index.map(str)
labeled_raw_data["sample_id"] = labeled_raw_data.index
labeled_raw_data.reindex()


raw_data_fns = [(r"../data/15_9-F-1 A_BIOSTRAT_RAW_1.DEX", "15_9-F-1 A"), 
                (r"../data/15_9-F-1 B_BIOSTRAT_RAW_1.DEX", "15_9-F-1 B"),
                (r"../data/15_9-F-1_BIOSTRAT_RAW_1.DEX", "15_9-F-1"),
                (r"../data/15_9-F-11 A_BIOSTRAT_RAW_1.DEX", "15_9-F-11 A"),
                (r"../data/15_9-F-11 B_BIOSTRAT_RAW_1.DEX", "15_9-F-11 B")
              ]
unlabeled_raw_data = pd.concat([get_dex_as_dataframe(*fn) for fn in raw_data_fns], sort=True)
unlabeled_raw_data=unlabeled_raw_data.replace(np.nan, 0)
unlabeled_raw_data["sample_id"] = unlabeled_raw_data.index
unlabeled_raw_data.reindex()

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    sorted_labeled_raw_data = labeled_raw_data.sort_values(by="age")
    
    fossils_occuring = (sorted_labeled_raw_data.values[:,:-2]>0)
    matrix_width = fossils_occuring.shape[1]
    well_matrix = np.stack([sorted_labeled_raw_data["Well_name"].values]*matrix_width, axis=1)
    wm1 = (well_matrix == "15_9-F-1 A") | (well_matrix == "15_9-F-1 B")
    wm2 = (well_matrix == "15_9-F-1") | (well_matrix == "15_9-F-11 A")
    wm3 = (well_matrix == "15_9-F-11 B")
    plt.imshow(np.dstack((fossils_occuring*wm1, fossils_occuring*wm2, fossils_occuring*wm3))*256, aspect=4)
    plt.show()
    
    plt.imshow((unlabeled_raw_data.values[:,:-1]>0).astype(int), aspect=4)
    
    plt.show()
