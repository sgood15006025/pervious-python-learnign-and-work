import csv

class Convert_LoL_to_CSV:
    """Creation of a class that will allow a conoversion of list of lists to csv"""

    def __init__(self, lol_name, converted_csv_filename):
        """Initialise that attributes of the list of lists name that you wish to convert to csv and
         the name of that you wih the csv file to be stored under"""
        self.lists_name = lol_name
        self.filename = converted_csv_filename

    def convert(self):
        """Convert the list of lists into the wanted csv file"""
        with open(f"{self.filename}.csv", 'w', newline= '') as f:
            writer = csv.writer(f)
            writer.writerows(self.lists_name)

