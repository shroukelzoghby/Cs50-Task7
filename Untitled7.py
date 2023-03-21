#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Linear search
import sys 
names= ["shrouk","omar","nada","ali"]
if "shrouk" in names:
    print("Found")
    sys.exit(0)
print("Not Found")
sys.exit(1)


# In[5]:


#Phonebook
people ={
    "salma":"092823",
    "ahmed":"0382",
    "zayn":"6161"
}
name= input("Name: ")
if name in people:
    print(f"Number: { people[name] }")


# In[14]:


import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()


# In[ ]:





# In[ ]:




