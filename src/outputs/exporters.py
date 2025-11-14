thonpython
import csv
import json
import pandas as pd

def export_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def export_csv(data, path):
    if not data:
        return
    keys = data[0].keys()
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

def export_excel(data, path):
    df = pd.DataFrame(data)
    df.to_excel(path, index=False)