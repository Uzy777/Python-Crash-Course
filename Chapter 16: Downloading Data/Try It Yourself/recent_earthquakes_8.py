# 16-8. Recent Earthquakes:     You can find online data files containing information about the most recent earthquakes over 1-hour, 1-day, 7-day, and 30-day periods.
#                               Go to https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php and you'll see a list of links to datasets for various time periods,
#                               focusing on earth-quakes of different magnitudes. Download one of these datasets and create a visualisation of the most recent earthquake activity.

from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path(
    "/home/uzy/Coding/Python-Crash-Course/Chapter 16: Downloading Data/eq_data/all_month_eq.geojson"
)
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
path = Path('/home/uzy/Coding/Python-Crash-Course/Chapter 16: Downloading Data/eq_data/readable_eq_data_tryityourself.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data["features"]
print(len(all_eq_dicts))

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    if mag is not None and mag > 0:  # Ensure magnitude is positive
        lon = eq_dict["geometry"]["coordinates"][0]
        lat = eq_dict["geometry"]["coordinates"][1]
        eq_title = eq_dict['properties']['title']
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
        eq_titles.append(eq_title)

print(mags[:10])
print(lons[:5])
print(lats[:5])


title = "Global Earthquakes"
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    title=title,
    color=mags,
    color_continuous_scale="Viridis",
    labels={"color": "Magnitude"},
    projection="natural earth",
    hover_name=eq_titles,
)
fig.show()
