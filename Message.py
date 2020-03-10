#!/usr/bin/env python
# coding: utf-8

# In[10]:


from textmagic.rest import TextmagicRestClient
  
username = "adwaittoro"
token = "wdoV7owy7F7BEBOm2eqOR1GghZfeEh"
client = TextmagicRestClient(username, token)

message = client.messages.create(phones="+19495617269", text="Hello")


# In[ ]:




