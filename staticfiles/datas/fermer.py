import csv
import json

csv_file = "/home/nihadtag/FarmAz/core/static/datas/uzum.csv"
json_file = "uzum.json"

data = []

with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        entry = {"Göstərici": row["Göstərici"]}
        for year, value in row.items():
            if year != "Göstərici":
                try:
                    entry[year] = float(value)
                except ValueError:
                    entry[year] = value  # keep as string if not a number
        data.append(entry)

# Write JSON
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("CSV successfully converted to JSON!")
