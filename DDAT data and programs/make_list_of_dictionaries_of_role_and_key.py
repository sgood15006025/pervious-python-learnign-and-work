import csv

filename = "Data/ddat-profession-capability-framework-role.csv"

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
        if d['Header'] == "ddat-profession-capability-framework-role":
            key_column = int(d["Index"])
        elif d['Header'] == 'name':
            role_column = int(d["Index"])

    # Build of list of dictionaries with roles and their corresponding key
    role_and_key_list = []
    for row in reader:
        role = row[role_column]
        key = row[key_column]
        role_key_dict = {"Key" : key, "Role" : role}
        role_and_key_list.append(role_key_dict)

