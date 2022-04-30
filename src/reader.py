# standard library
import json

# 3rd party library
import pandas as pd
from tqdm import tqdm

# read json file from a provided path
def read_json(path_json):
    """
    Return a dataframe, given a JSON filepath.
    """
    # create an empty DataFrame object
    df_data = pd.DataFrame(columns = ["site", "campaign", "faq", 
                                      "update", "comment", "community"])

    # opening JSON file
    with open(path_json) as json_file:
        dict_data = json.load(json_file)

    # append rows to an empty DataFrame   
    for _, v in tqdm(dict_data.items()):
        df_data = df_data.append({"site": v["site"],
                                  "campaign": v["campaign"],
                                  "faq": v["faq"], 
                                  "update": v["update"],
                                  "comment": v["comment"],
                                  "community": v["community"]}, 
                                 ignore_index = True)
    
    return df_data