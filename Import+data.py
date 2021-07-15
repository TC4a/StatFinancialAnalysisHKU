
# coding: utf-8

# # Import data
# In this Jupyter Notebook, you will learn how to import data from CSV into Jupyter Notebook

# In[13]:


#import the package "Pandas" into Jupyter Notebook
import pandas as pd


# In[14]:


#We import the stock data of Facebook into Jupyter Notebook. The CSV file is located in the folder called "Data" in your Workspace
#We then name the DataFrame name as 'fb'
fb = pd.DataFrame.from_csv('../data/facebook.csv')


# ### Instruction
# Now is your turn to import the stock price of Microsoft (microsoft.csv), of which the CSV is located in the same folder, and rename the Dataframe in "ms". 

# In[13]:


ms = none


# In[14]:


# run this cell to ensure Microsoft's stock data is imported
print(ms.iloc[0, 0])


# ** Expected output: ** 46.73

# In[ ]:




