import pandas as pd
import plotly.express as px
file = pd.read_csv(r"C:\\Users\\devinhill\\Downloads\\Titanic_Data1.csv")
graph = px.histogram(
file, 
x='Survived',
y='Age',
color='Sex',
barmode='group',
text_auto=True,
title='Titanic')
graph.show()
