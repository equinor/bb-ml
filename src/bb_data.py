import pandas as pd
import numpy as np
from parse_computed import get_interval_df
from raw_dex_reader import get_dex_as_dataframe as get_dex_as_dataframe2

def get_dex_as_dataframe(fn, well_name):
    raw = get_dex_as_dataframe2(fn)
    raw["Well_name"] = well_name
    return raw

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
    labeled_samples = raw.dropna()
    return labeled_samples

test1 = get_labeled_raw_data(r"../data/15_9-F-1 A_BIOSTRAT_RAW_1.DEX", r"../data/15_9-F-1 A_BIOSTRAT_COMPUTED_1.DEX", "15_9-F-1 A")
test2 = get_labeled_raw_data(r"../data/15_9-F-1 B_BIOSTRAT_RAW_1.DEX", r"../data/15_9-F-1 B_BIOSTRAT_COMPUTED_1.DEX", "15_9-F-1 B")
test3 = get_labeled_raw_data(r"../data/15_9-F-1_BIOSTRAT_RAW_1.DEX", r"../data/15_9-F-1_BIOSTRAT_COMPUTED_1.DEX", "15_9-F-1")
test4 = get_labeled_raw_data(r"../data/15_9-F-11 A_BIOSTRAT_RAW_1.DEX", r"../data/15_9-F-11 A_BIOSTRAT_COMPUTED_1.DEX", "15_9-F-11 A")
test5 = get_labeled_raw_data(r"../data/15_9-F-11 B_BIOSTRAT_RAW_1.DEX", r"../data/15_9-F-11 B_BIOSTRAT_COMPUTED_1.DEX", "15_9-F-11 B")
label_raw_data = pd.concat([test1, test2,test3,test4,test5], sort=True)
label_raw_data=label_raw_data.replace(np.nan, 0)


raw_data_fns = [(r"../data/15_9-F-1 A_BIOSTRAT_RAW_1.DEX", "15_9-F-1 A"), 
                (r"../data/15_9-F-1 B_BIOSTRAT_RAW_1.DEX", "15_9-F-1 B"),
                (r"../data/15_9-F-1_BIOSTRAT_RAW_1.DEX", "15_9-F-1"),
                (r"../data/15_9-F-11 A_BIOSTRAT_RAW_1.DEX", "15_9-F-11 A"),
                (r"../data/15_9-F-11 B_BIOSTRAT_RAW_1.DEX", "15_9-F-11 B")
              ]
unlabeled_raw_data = pd.concat([get_dex_as_dataframe(*fn) for fn in raw_data_fns], sort=True)
unlabeled_raw_data=unlabeled_raw_data.replace(np.nan, 0)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    plt.imshow((label_raw_data.values[:,:-2]>0).astype(int), aspect=4)
    plt.show()
    
    plt.imshow((unlabeled_raw_data.values[:,:-1]>0).astype(int), aspect=4)
    
    plt.show()
