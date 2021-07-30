import csv

from build_list_of_job_roles import job_roles
filename = "Data/ddat-jobs-and-skills-list-PMG.csv"



class Role:
    """A simple attempt to model a role"""

    def __init__(self, role):
        """Initialise name attribute"""
        self.role = role

    def find_skills(self):
        """Find all the skills realating to a role"""
        with open(filename) as f:
            reader = csv.reader(f)

            role = self.role
            list_of_roll_and_skills = []
            list_of_roll_and_skills.append(role)
            for row in reader:
                if row[3] == role:
                    if row[3] in list_of_roll_and_skills:
                        list_of_roll_and_skills.append(row[6])
        return(list_of_roll_and_skills)


list_of_lists_of_job_role_and_skills = []
for role in job_roles:
    my_role = Role(role)
    list_of_lists_of_job_role_and_skills.append(my_role.find_skills())

print(list_of_lists_of_job_role_and_skills)





