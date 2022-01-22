import json, pandas as pd
from pathlib import Path

# solving problems with linux and windows directories
config = json.load(open(Path("config.json"),'r'))
# detail or price
fileconfig = lambda key : Path("base",config[key])

filecsv = pd.read_csv(fileconfig('price'))
print(filecsv)