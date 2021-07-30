import csv

filename = "Data/ddat-profession-capability-framework-job-family.csv"

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
        if d['Header'] == "ddat-profession-capability-framework-job-family":
            key_column = int(d["Index"])
        elif d['Header'] == 'name':
            job_family_column = int(d["Index"])

    # Build of list of dictionaries with job families and their corresponding key
    job_family_and_key_list = []
    for row in reader:
        job_family = row[job_family_column]
        key = row[key_column]
        job_family_key_dict = {"Key" : key, "Job family" : job_family}
        job_family_and_key_list.append(job_family_key_dict)

