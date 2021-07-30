import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
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

    # Search through the list of headers for a specific header and record the index number
    for d in header_row_dict_list:
        if d["Header"] == "TMAX":
            highs_column = int(d["Index"])
        elif d["Header"] == "TMIN":
            lows_column = int(d['Index'])
        elif d["Header"] == "DATE":
            date_column = int(d["Index"])
        elif d["Header"] == "NAME":
            name_column = int(d['Index'])


    # Get dates, high and low tempuratures from this file and a name for the area.
    dates, highs, lows = [], [], []
    line_read = 0
    for row in reader:
        current_date = datetime.strptime(row[date_column], '%Y-%m-%d')
        # Specify the name from just one row
        if line_read == 0:
            name = row[name_column]
            line_read += 1

        try:
            high = int(row[highs_column])
            low = int(row[lows_column])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
plt.title(f"Daily high and low temperatures, 2018\n{name.title()}", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

