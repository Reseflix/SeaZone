import json, pandas as pd
from pathlib import Path

def main():
    # solving problems with linux and windows directories
    config = json.load(open(Path("config.json"),"r"))
    # detail or price
    fileconfig = lambda key : Path("base",config[key])
    # opening
    detail = pd.read_csv(fileconfig("detail"),encoding="utf-8").drop(columns=["Unnamed: 0"])
    price = pd.read_csv(fileconfig("price"),encoding="utf-8").drop(columns=["Unnamed: 0","Unnamed: 0.1"])
    # Concat
    conc = pd.merge(price,detail,"inner",["airbnb_listing_id"])
    conc["mean"] = conc[["airbnb_listing_id","price_string"]].groupby("airbnb_listing_id").transform("mean")
    conc = conc.sort_values(["airbnb_listing_id","suburb","mean"]).drop(columns=["mean"])
    # Save 
    conc.to_csv(Path("result","conc.csv"),sep=";",index=False)