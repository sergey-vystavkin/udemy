from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
import plotly.graph_objects as go
import pandas as pd

# DATA
df = pd.read_csv('2011_US_AGRI_Exports')

data = dict(type='choropleth',
            locations=['AZ', 'CA', 'NY'],
            locationmode='USA-states',
            colorscale='Jet',
            text=['Arizona', 'Cali', 'New York'],
            z=[1.0, 2.0, 3.0],
            colorbar={'title': 'Colorbar Title Goes Here'})

# colorscale - color style (Portland, Jet, Greens, ylorrd)

layout = dict(geo={'scope': 'usa'})  # Part of world (world, usa, europe, asia, africa, north america, south america)
choromap = go.Figure(data=[data], layout=layout)


data = dict(type='choropleth',
            locations=df['code'],
            locationmode='USA-states',
            colorscale='ylorrd',
            text=df['text'],
            z=df['total exports'],
            colorbar={'title': 'Millions USD'},
            marker=dict(line=dict(color='rgb(255, 255, 255)', width=2))
            )
# marker - borders style

layout = dict(title='2011 US Agriculture Exports by State',
              geo={'scope': 'usa', 'showlakes': True, 'lakecolor': 'rgb(85, 173, 240)'})

choromap_2 = go.Figure(data=[data], layout=layout)

iplot(choromap_2)


