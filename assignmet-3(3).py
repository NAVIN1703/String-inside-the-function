#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def upp_lower(string):
    upperwords=0
    lowerwords=0
    for char in string:
        if char.isupper():
            upperwords=upperwords+1
        elif char.islower():
            lowerwords=lowerwords+1
    print(" No. of upper case character:",upperwords)
    print("No. of lower case character:",lowerwords)
upp_lower("The quick Brow Fox")

