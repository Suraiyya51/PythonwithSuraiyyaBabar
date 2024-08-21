#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt

# Example DataFrame
import pandas as pd
import numpy as np

# Create a sample DataFrame
np.random.seed(42)
data = pd.DataFrame({
    'category': np.random.choice(['A', 'B', 'C'], size=100),
    'value': np.random.randn(100)
})

# Create a FacetGrid and map a boxplot to it
g = sns.FacetGrid(data, col="category", col_wrap=3, height=4)
g.map(sns.boxplot, 'value')

plt.show()


# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt

# Example DataFrame
import pandas as pd
import numpy as np

# Create a sample DataFrame
np.random.seed(42)
data = pd.DataFrame({
    'category1': np.random.choice(['A', 'B', 'C'], size=100),
    'category2': np.random.choice(['X', 'Y'], size=100),
    'value': np.random.randn(100)
})

# Create a FacetGrid and map a boxplot to it
g = sns.FacetGrid(data, row="category1", col="category2", height=4)
g.map(sns.boxplot, 'value')

plt.show()


# In[ ]:




