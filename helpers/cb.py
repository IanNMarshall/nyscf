# import geopandas as gp
# import pandas as pd
# import plotly.offline as py
# import json
# import sys, os


import plotly.offline as py
import plotly.graph_objs as go
import numpy as np
import colorlover as cl

purp = cl.scales['9']['seq']['Purples']
purp2 = [[0, purp[0]], [1,purp[-1]]]
r = np.random.randn(20)

trace1 = go.Scatter(
    y = r,
    mode='markers',
    marker=dict(
        size=16,
        color = r, 
        colorscale=purp2,
        showscale=True
    )
)
data = [trace1]
# Plot and embed in ipython notebook!
print(trace1['marker'])
py.plot(data, filename='basic-scatter.html')
#