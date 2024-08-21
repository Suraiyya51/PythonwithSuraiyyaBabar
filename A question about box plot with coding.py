#!/usr/bin/env python
# coding: utf-8

# In[3]:


import seaborn as sns
import pandas as pd
import numpy as np
kashti = sns.load_dataset("titanic")
kashti.head(15)


# In[17]:


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

kashti = sns.load_dataset("titanic")
plt=sns.boxplot(x ="embark_town",y= "fare",hue="class",palette="Blues",data=kashti)
plt.show()


# In[ ]:


# iss baat ki samjh nahee aa rahi . error bhi dey raha h aur plot bhi show kr raha h


# In[15]:


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # Import matplotlib for plotting

# Load the Titanic dataset
kashti = sns.load_dataset("titanic")

# Create the boxplot
sns.boxplot(x="embark_town", y="fare", hue="class", palette="Blues", data=kashti)

# Display the plot
plt.show()


# In[ ]:


#iss ka tw chat g pt se poochha . uss ne ye code bta diya . phir m ne khud code likha tw wo error dey raha h.

