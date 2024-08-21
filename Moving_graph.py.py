#!/usr/bin/env python
# coding: utf-8

# In[10]:



import plotly.express as px
import pandas as pd

# Sample data similar to Gapminder
data = {
    'country': ['Afghanistan', 'Brazil', 'China', 'Denmark', 'Egypt'],
    'continent': ['Asia', 'South America', 'Asia', 'Europe', 'Africa'],
    'year': [2007, 2007, 2007, 2007, 2007],
    'gdpPercap': [974.5803384, 9065.800825, 4959.114854, 35278.41874, 5581.180998]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar plot
fig = px.bar(df, x='country', y='gdpPercap', color='continent', title='GDP per Capita in 2007')

# Show the plot
fig.show()


# In[11]:


import plotly.express as px
import pandas as pd

# Sample data similar to Gapminder
data = {
    'country': ['Afghanistan', 'Brazil', 'China', 'Denmark', 'Egypt'],
    'continent': ['Asia', 'South America', 'Asia', 'Europe', 'Africa'],
    'year': [2007, 2007, 2007, 2007, 2007],
    'gdpPercap': [974.5803384, 9065.800825, 4959.114854, 35278.41874, 5581.180998]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar plot
fig = px.scatter(df, x='country', y='gdpPercap', color='continent', title='GDP per Capita in 2007')

# Show the plot
fig.show()


# In[ ]:




