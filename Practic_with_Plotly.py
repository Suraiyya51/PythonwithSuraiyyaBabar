#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.express as px
suraiyya = px.data.iris()
fig = px.scatter_3d(suraiyya, x='sepal_length', y='sepal_width', z='petal_width',
                    color='petal_length', symbol='species',title="This practice is done by Suraiyya Babar")
fig.show()


# In[ ]:


# It is from seaborn lib (above Plot)


# In[2]:


import seaborn as sns
sns.set_theme(style="ticks")
suraiyya = sns.load_dataset("mpg")
print(suraiyya)

colors = (250, 70, 50), (350, 70, 50)
cmap = sns.blend_palette(colors, input="husl", as_cmap=True)
sns.displot(
    suraiyya,
    x="displacement", col="origin", hue="model_year",
    kind="ecdf", aspect=.75, linewidth=2, palette=cmap,
)


# In[ ]:


# Plot with changing values


# In[3]:


import seaborn as sns
sns.set_theme(style="ticks")
jabeen = sns.load_dataset("mpg")
print(jabeen)

colors = (250, 70, 50), (350, 70, 50)
cmap = sns.blend_palette(colors, input="husl", as_cmap=True)
sns.displot(
    jabeen,
    x="horsepower", col="origin", hue="acceleration",
    kind="ecdf", aspect=.75, linewidth=5, palette=cmap,
)


# In[5]:


colors = (250, 70, 50), (350, 70, 50)
cmap = sns.blend_palette(colors, input="husl", as_cmap=True)
sns.displot(
    jabeen,
    x="acceleration", col="origin", hue="horsepower",
    kind="ecdf", aspect=.75, linewidth=2, palette=cmap,
)


# In[8]:


colors = (250, 70, 50), (350, 70, 50)
cmap = sns.blend_palette(colors, input="husl", as_cmap=True)
sns.displot(
    jabeen,
    x="origin", col="horsepower", hue="model_year",
    kind="ecdf", aspect=.75, linewidth=2, palette=cmap,
)


# In[ ]:


# tw kuch kaam nahee ho skey ga 

