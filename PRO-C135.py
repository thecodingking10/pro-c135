import csv
import plotly.express as px

rows = []

with open('final.csv', 'r') as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        rows.append(i)

headers = rows[0]
star_data_rows = rows[1:]

star_name = []
star_mass = []
star_radius = []
star_distance = []
star_gravity = []

for star_data in star_data_rows:
    star_name.append(star_data[1])
    star_mass.append(star_data[3])
    star_radius.append(star_data[4])
    star_distance.append(star_data[2])
    star_gravity.append(star_data[5])

fig = px.bar(x=star_name, y=star_mass, title="Star Masses")
fig.show()

fig = px.bar(x=star_name, y=star_radius, title="Star Radii")
fig.show()

fig = px.bar(x=star_name, y=star_distance, title="Star Distance")
fig.show()

fig = px.bar(x=star_name, y=star_gravity, title="Star Gravity")
fig.show()
