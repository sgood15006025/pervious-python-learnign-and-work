import csv

from make_a_list_of_dictionaries_of_level_and_key import level_and_key_list
from make_a_list_of_dictionaries_of_skill_and_key import skill_and_key_list
from make_a_list_of_dictionaries_of_skill_type_and_key import skill_type_and_key_list
from make_list_of_dictionaries_of_job_family_and_key import job_family_and_key_list
from make_list_of_dictionaries_of_role_and_key import role_and_key_list
from make_list_of_dictionaries_of_role_level_and_key import role_level_and_key_list

filename = "Data/ddat-profession-capability-framework.csv"

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

    job_and_skill_info_list = []

    for row in reader:
        job_and_skill_info = []
        skill_type_key = int(row[5][-2:])
        job_family_key = int(row[6][-3:])
        role_key = int(row[7][-4:])
        role_level_key = int(row[8][-4:])
        skill_key = (row[9][-4:])
        level_key = row[10][-3:]

        for s_t in skill_type_and_key_list:
            if skill_type_key == int(s_t["Key"]):
                required_skill_type = s_t["Skill type"]
                job_and_skill_info.append(required_skill_type)

        for j_f in job_family_and_key_list:
            if job_family_key == int(j_f["Key"]):
                required_job_family = j_f["Job family"]
                job_and_skill_info.append(required_job_family)

        for r in role_and_key_list:
            if role_key == int(r["Key"]):
                required_role = r['Role']
                job_and_skill_info.append(required_role)

        for r_l in role_level_and_key_list:
            if role_level_key == int(r_l["Key"]):
                required_role_level = r_l["Role level"]
                job_and_skill_info.append(required_role_level)

        for s in skill_and_key_list:
            if skill_key == s["Key"]:
                required_skill = s["Skill"]
                job_and_skill_info.append(required_skill)

        for l in level_and_key_list:
            if level_key == l["Key"]:
                required_level = l["Level"]
                job_and_skill_info.append(required_level)

        job_and_skill_info_list.append(job_and_skill_info)
