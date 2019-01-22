import plotly
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv("Nutrition_Results2.csv")
cols = df.columns 


data = []
for index, row in df.iterrows():
    trace = go.Bar(
         x=cols,
         y=row,
         name="Item " + str(index)
    )
    data.append(trace)    
    

layout = go.Layout(
    barmode='stack'
)


plotly.offline.plot({
    "data": data,
    "layout": layout}
, auto_open=True)