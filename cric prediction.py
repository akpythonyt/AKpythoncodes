import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

data = pd.read_csv('Sample scores.csv')
from sklearn.linear_model import LinearRegression
# x and y given as array_like objects
import plotly.express as px
fig = px.scatter(data,x='Overs', y='Scores')
fig.show()

linear_reg = LinearRegression()
x = data.Overs.values.reshape(-1,1)
y = data.Scores.values.reshape(-1,1)
linear_reg.fit(x,y)

next_salary = linear_reg.predict([[19]])
print(int(next_salary))