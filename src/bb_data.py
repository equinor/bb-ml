import pandas as pd
import numpy as np
from parse_computed import get_interval_df
from raw_dex_reader import get_dex_as_dataframe

def get_labeled_raw_data(fn_raw_data, fn_computed_data):
    raw = get_dex_as_dataframe(fn_raw_data)
    computed_interval = get_interval_df(fn_computed_data)
    
    chronostratigraphic_df = computed_interval[computed_interval["Type"]=="Chronostratigraphy"]
    
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

test = get_labeled_raw_data(r"../data/15_9-F-1 A_BIOSTRAT_RAW_1.DEX", r"../data/15_9-F-1 A_BIOSTRAT_COMPUTED_1.DEX")
#test2 = get_labeled_raw_data(r"../data/15_9-F-1 B_BIOSTRAT_RAW_1.DEX", r"../data/15_9-F-1 B_BIOSTRAT_COMPUTED_1.DEX")