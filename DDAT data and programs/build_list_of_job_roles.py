import csv

filename = "Data/ddat-jobs-and-skills-list-PMG.csv"
with open(filename) as f:
    reader = csv.reader(f)

    # Make a list of all the roles
    job_roles = []
    for row in reader:
        if row[3] not in job_roles:
            job_roles.append(row[3])
