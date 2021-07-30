import csv

filename = "Data/ddat-profession-capability-framework-level.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Generate a list of dictionaries detailing the header and the index number
    header_row_dict_list = []
    for index, columnheader in enumerate(header_row):
        header_row_dict = {}
        header_row_dict["Header"] = columnheader
        header_row_dict["Index"] = index
        header_row_dict_list.append(header_row_dict)


    # Search for specific row index we want
    for d in header_row_dict_list:
        if d['Header'] == "ddat-profession-capability-framework-level":
            key_column = int(d["Index"])
        elif d['Header'] == 'name':
            level_column = int(d["Index"])

    # Build of list of dictionaries with roles and their corresponding key
    level_and_key_list = []
    for row in reader:
        level = row[level_column]
        key = row[key_column]
        level_key_dict = {"Key" : key, "Level" :level}
        level_and_key_list.append(level_key_dict)


