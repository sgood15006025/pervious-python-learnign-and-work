import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "data/world_fires_1_day.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lats, lons, brightnesses, = [], [], []
    for row in reader:
        lats.append(row[0])
        lons.append(row[1])
        brightnesses.append(row[2])

# Map fires

data = [{'type' : 'scattergeo',
         'lon': lons,
         'lat': lats,
         'marker': {
             'size': [float(brightness)/5 for brightness in brightnesses],
             'color': brightnesses,
             'colorscale': 'Cividis',
             'reversescale': True,
             'colorbar': {'title': 'Brightness'}
         },
         }]

#plot data
my_layout = Layout(title= 'Global fires')

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename='global_fires.html')
