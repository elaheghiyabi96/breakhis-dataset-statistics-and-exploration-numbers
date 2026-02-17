#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os

def print_tree(path, indent=""):
    for f in os.listdir(path):
        full_path = os.path.join(path, f)
        if os.path.isdir(full_path):
            print(indent + "|-- " + f)
            print_tree(full_path, indent + "    ")

dataset_root = r"D:\Breast cancer\dataset_cancer_v1\dataset_cancer_v1"
print_tree(dataset_root)




# In[ ]:




