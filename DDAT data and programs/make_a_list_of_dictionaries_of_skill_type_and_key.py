import csv

filename = "Data/ddat-profession-capability-framework-skill-type.csv"

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
        if d['Header'] == "ddat-profession-capability-framework-skill-type":
            key_column = int(d["Index"])
        elif d['Header'] == 'name':
            skill_type_column = int(d["Index"])

    # Build of list of dictionaries with roles and their corresponding key
    skill_type_and_key_list = []
    for row in reader:
        skill_type = row[skill_type_column]
        key = row[key_column]
        skill_type_key_dict = {"Key" : key, "Skill type" : skill_type}
        skill_type_and_key_list.append(skill_type_key_dict)

