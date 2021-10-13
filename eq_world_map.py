import json

from plotly.graph_objs._scattergeo import Scattergeo
from plotly.graph_objs._layout import Layout
from plotly import offline

filename = 'eq-data\eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict  in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

#Mapa trzesień ziemi
data = [{
    'type': 'scattergeo',
    'lon': lons, 
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags]
}, }]
my_layout = Layout(title='Trzęsienia ziemi na świecie')

fig = {'data': data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquakes.html')