import plotly.plotly as py
from plotly.graph_objs import *
import pandas as pd

# Import data from csv
df = pd.read_csv('C:/Hary/Bigdata/Apache/Data/Korean/0_0_0.csv', encoding = "ISO-8859-1")
df.head()
x1=df['name']
y1=df['latitude']
z1=df['longitude']
print(x1)
print(y1)
print(z1)

trace1 = {
  "lat": y1,
  "locationmode": "USA-states",
  "lon": z1,
  "marker": {
    "color": [4.8, 3.9, 3.6, 4.1, 0, 4, 0, 4.8, 4.1, 0, 4.4, 0, 4.2, 4.6, 0, 4.6, 4.4, 0, 0, 0, 2.9, 0, 4.5, 4.3, 0, 0, 0, 0, 0, 4.1, 0, 0, 0, 0, 4.5, 0, 0, 0, 0, 4.6, 3.9, 3.8, 3.8, 3.8, 3.8, 3.5, 4.7, 0, 3.4, 4, 4, 4.2, 4.6, 4, 4.1, 4.2, 4.7, 0, 4.6, 4.1, 4, 4, 0, 3.1, 3.8, 0, 4.6, 3.2, 0, 4.3, 4.3, 4.1, 0, 3.8, 4.6, 0, 4.1, 4.1, 4.3, 4.4, 4.3, 3.6, 4.1, 3.8, 4, 4.4, 4.4, 4.1, 4.1, 4.3, 4.3, 4.2, 0, 4.2, 4, 4.9, 4.1, 0, 4.4, 4.7, 4.4, 0, 3.7, 0, 0, 3.9, 0, 0, 4, 2.6, 4.6, 2.5, 4, 4.4, 4.3, 4.3, 4.2, 3.4, 4.4, 0, 3.3, 0, 4.4, 4.1, 4.3, 0, 4.6, 4.3, 4.3, 4.6, 0, 3, 4.4, 4.5, 3.1, 3.8, 0, 4.2, 4, 4.4, 4.8, 0, 4.5, 3.9, 3.9, 4.3, 4.1, 4.4, 0, 4.2, 0, 4.3, 0, 0, 3.1, 4.4, 4.2, 4.3, 4.5, 4.5, 3.9, 4.5, 4.2, 3.9, 4, 4.5, 4.2, 4.3, 4.2, 0, 3.7, 4.1, 4.2, 4, 4.3, 4.4, 4.3, 3.5, 4.3, 3.9, 4.3, 3.8, 4.4, 4.1, 0, 4.1, 0, 3.9, 0, 0, 3.9, 4, 4.9, 0, 0, 3.8, 4.5, 3.8, 3.9, 0, 4.2, 0, 0, 4.3, 0, 4, 0, 4.6, 4.7, 0, 4.7, 0, 0, 0, 0, 4.3, 4, 3.7, 4.1, 3, 2.6, 4.2, 3.8, 4.1, 4.6, 4.1, 4.2, 4.1, 4.2, 3.2, 2.6, 4.7, 4.1, 3.4, 2.2, 4.2, 3.5, 3.2, 4.4, 3.8, 3.2, 4.4, 4, 3.8, 4.4, 3.2, 3.8, 4.2, 3.1, 4.4, 3, 4.4, 3.2, 3.2, 3.3, 4.6, 3.3, 3.7, 0, 3, 4.2, 4.3, 4.2, 4.1, 4.3, 3.9, 4, 4.2, 3.8, 4.3, 0, 3.1, 4, 4.4, 0, 3.1, 4.3, 4.2, 4.8, 4.4, 0, 4.3, 4.1, 0, 3.9, 4.1, 3.9, 4.1, 0, 4.2, 4.1, 3.7, 3.2, 2.5, 4.2, 4.5, 4.4, 3.9, 3.6, 3.5, 2.6, 0, 0, 4.1, 4, 4.7, 4.3, 3.4, 4.4, 4, 4.3, 3.9, 4, 3.4, 3.2, 3.4, 4.5, 4, 4.1, 4.5, 4.1, 4.7, 3.6, 3.1, 3.8, 2.1, 3.9, 4.2, 3.2, 3.7, 4.3, 3.5, 0, 3.6, 3, 3.5, 3.4, 0, 4, 4.6, 3.1, 4.1, 4.2, 3, 4.1, 4.5, 3.8, 2.5, 4.6, 0, 3.4, 4.2, 3.5, 4.2, 3.6, 3.4, 4, 0, 0, 0, 4, 0, 0, 4.6, 0, 0, 0, 0, 0, 0, 3.2, 4, 3, 3.1, 3.8, 2.7, 3.2, 4.6, 3.4, 0, 3.5, 0, 0, 4, 4.2, 0, 0, 4.3, 2.8, 4.1, 4.3, 4, 0, 4, 0, 0, 3.9, 0, 4.2, 0, 3, 4, 0, 0, 0, 4.5, 0, 4.5, 0, 3.9, 3.8, 0, 3.9, 3.8, 3.4, 3.7, 0, 0, 4.6, 0, 4.1, 3.8, 0, 4, 4.3, 3.7, 0, 0, 4.5, 3.9, 4.2, 3.5, 4.1, 4.3, 2.6, 3.1, 3.6, 4.4, 3.9, 4.4, 3.6, 4.3, 4.5, 3.6, 3.7, 0, 4.3, 0, 2.6, 4, 4.1, 4.6, 0, 4.6, 3.6, 3.3, 3.5, 4.4, 4.3, 4.4, 3, 0, 3.5, 4.5, 3.9, 0, 4, 0, 0, 4.4, 4.4, 4, 4.2, 4.5, 2.7, 4.2, 3.5, 3.6, 0, 4.4, 3.9, 4.7, 3.9, 0, 3.4, 2.6, 4.2, 4.3, 3.6, 4.3, 4.4, 3.4, 4.3, 4, 4, 4.1, 0, 0, 3.7, 4.4, 3.2, 3.9, 3.8, 4.4, 0, 4.1, 3.9, 4.1, 4, 4.5, 3.1, 4.5, 4.4, 4.3, 3.4, 0, 0, 0, 0, 3.3, 3, 2.3, 2.7, 4, 3.9, 4.3, 3.2, 4.4, 4, 3.8, 3.1, 3.6, 3.8, 4.2, 3.7, 2.7, 2.9, 4.2, 3.3, 4.1, 3.3, 2.8, 0, 4, 4.4, 4, 4.3, 4.1, 0, 4, 0, 4.1, 0, 0, 0, 0, 3.9, 4.6, 4.5, 4.4, 4.1, 4.2, 4.3, 4.5, 3.8, 4, 4.4, 4.1, 4.3, 3.1, 4.2, 3, 3.8, 3.2, 4.4, 3.5, 4.4, 4.5, 4.5, 4.4, 4, 3.7, 3.8, 4.2, 4.1, 4.2, 4, 3.8, 4, 4.5, 3.6, 4.1, 4, 0, 4.6, 0, 0, 3.5, 0, 3.5, 4.1, 4.4, 4.6, 3.1, 4.8, 4.2, 3.6, 4.4, 4.1, 0, 3.3, 4.2, 4.7, 3.9, 4, 4.3, 0, 4.4, 4.3, 4.3, 0, 3.9, 0, 3.8, 0, 3.8, 0, 0, 3.2, 0, 0, 0, 4.9, 0, 4.4, 2.7, 2.9, 4.7, 4, 2.9, 3, 2.6, 0, 3.4, 3.7, 3.9, 3.4, 4.4, 3.1, 4.2, 0, 4.1, 4, 4, 0, 4.4, 4.1, 4.7, 4, 4.4, 3.5, 4.4, 3.9, 4, 4.3, 2.6, 4.1, 4, 4.5, 4.3, 3.8, 3.9, 3.7, 4.4, 3.5, 2.6, 3.9, 4, 0, 3.1, 3.4, 0, 4.2, 0, 4.3, 0, 0, 0, 4, 0, 4.4, 4.2, 4.3, 3.9, 4, 0, 4, 3.9, 4.8, 4.2, 4.1, 4.2, 4.4, 4.4, 3.8, 3.7, 3.2, 4.3, 4.4, 4.1, 3.7, 4.5, 3.8, 4.2, 4.3, 4.3, 0, 0, 4.5, 0, 0, 4.2, 3.9, 0, 0, 4, 0, 3.8, 0, 4, 0, 4.6, 4.2, 4, 3.5, 3.1, 3.9, 4.2, 4.1, 3.8, 4.8, 4.1, 0, 3.2, 4, 3.9, 2.3, 0, 3.2, 3.8, 3.6, 3.7, 3.9, 4.2, 4.3, 3.7, 4.1, 3.5, 3.3, 2.9, 3.2, 3.6, 2.9, 0, 4.2, 3.4, 4.2, 4.2, 2.2, 3.4, 4.3, 0, 0, 0, 4.1, 4.3, 4.4, 0, 0, 3, 0, 4.3, 4, 0, 3.2, 0, 4.3, 0, 0, 0],
    "colorbar": {"title": "Restuarant Rating"},
    "colorscale": [
      [0, "#440154"], [0.111111111111, "#482878"], [0.222222222222, "#3E4A89"], [0.333333333333, "#31688E"], [0.444444444444, "#26838E"], [0.555555555556, "#1F9D89"], [0.666666666667, "#35B779"], [0.777777777778, "#6CCE59"], [0.888888888889, "#B4DD2C"], [1, "#FDE725"]]
  },
  "mode": "markers",
  "text": x1,
  "type": "scattergeo"
}

data = Data([trace1])
layout = {
  "geo": {
    "countrycolor": "rgb(217,217,217)",
    "countrywidth": 0.5,
    "landcolor": "rgb(242,242,242)",
    "projection": {"type": "albers usa"},
    "scope": "usa",
    "showland": True,
    "subunitcolor": "rgb(217,217,217)",
    "subunitwidth": 0.5
  },
  "title": "Korean Restaurants in the US"
}

fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)