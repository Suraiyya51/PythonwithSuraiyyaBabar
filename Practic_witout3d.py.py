#!/usr/bin/env python
# coding: utf-8

# In[6]:


import seaborn as sns
sns.set_theme()

# Load the example dataset for Anscombe's quartet
suraiyya = sns.load_dataset("anscombe")
print(suraiyya)

# Show the results of a linear regression within each dataset
sns.lmplot(
    data=suraiyya, x="x", y="y", col="dataset", hue="dataset",
    col_wrap=3, palette="deep", ci=True,
    height=4, scatter_kws={"s": 50, "alpha": 1}
)


# In[ ]:


# kia is m TITLE ka attribute nahee h ??? title deney pr error dey diya


# In[8]:


import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="darkgrid")

# Load the example diamonds dataset
heeray = sns.load_dataset("diamonds")

# Draw a scatter plot while assigning point colors and sizes to different
# variables in the dataset
f, ax = plt.subplots(figsize=(8.5, 4.5))
sns.despine(f, left=True, bottom=True)
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
sns.scatterplot(x="carat", y="price",
                hue="clarity", size="depth",
                palette="ch:r=-.2,d=.3_r",
                hue_order=clarity_ranking,
                sizes=(4, 8), linewidth=5,
                data=heeray, ax=ax)


# In[10]:


import seaborn as sns
sns.set_theme(style="darkgrid")

# Load an example dataset with long-form data
marzi = sns.load_dataset("fmri")

# Plot the responses for different events and regions
sns.lineplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=marzi)


# In[11]:


import seaborn as sns
sns.set_theme(style="ticks")

points = sns.load_dataset("dots")

# Define the palette as a list to specify exact values
palette = sns.color_palette("rocket_r")

# Plot the lines on two facets
sns.relplot(
    data=points,
    x="time", y="firing_rate",
    hue="coherence", size="choice",  col="align",
    kind="line", size_order=["T1", "T2"], palette=palette,
    height=8, aspect=.90, facet_kws=dict(sharex=False),
)


# In[14]:


import seaborn as sns
sns.set_theme(style="whitegrid")

penguins = sns.load_dataset("penguins")

# Draw a nested barplot by species and sex
g = sns.catplot(
    data=penguins, kind="bar",
    x="species", y="body_mass_g", hue="sex",
    errorbar="sd", palette="dark", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("", "Body mass (g)")
g.legend.set_title("")


# In[ ]:


# ye Plot samjh nahee aaya.

