# standard library
import json
import regex as re
from os import walk, path

# 3rd party library
import pandas as pd
from tqdm import tqdm

# read JSON file from a provided path
def read_json(path_json):
    """
    Return a dataframe, given a JSON filepath.
    """
    # create an empty DataFrame object
    df_data = pd.DataFrame(columns = ["site", "campaign", "faq", 
                                      "update", "comment", "community"])

    # open a JSON file
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

# extract url from a DataFrame
def extract_project_url(df_input):
    list_url = []
    for ele in df_input["urls"]:
        dict_tmp = json.loads(ele)
        str_tmp = dict_tmp["web"]["project"]
        list_url.append(re.split('\?', str_tmp)[0])
    return list_url

# read CSV files in a provided directory
def read_csv(dir_path_data):
    if path.exists(dir_path_data+"\Kickstarter.csv") is False:
        print("put Kickstarter.csv into data directory.")
    else:
        df_cp = pd.DataFrame()
        filenames = next(walk(dir_path_data), (None, None, []))[2]

        for ele in filenames:
            df_cp_tmp = pd.read_csv(dir_path_data + "\\" + ele)

            # a continuous index value will be maintained
            # across the rows in the new concatenated data frame.
            df_cp = pd.concat([df_cp, df_cp_tmp], ignore_index=True)
    
    list_site = extract_project_url(df_cp)
    df_cp["site"] = list_site

    return df_cp