#!/usr/bin/env python
# coding: utf-8

# In[1]:


answer = input("what's your name?")
print('hello,'+answer)


# In[2]:


i=0
while i<3:
    print("meow")
    i+=1


# In[3]:


for i in range(10):
    print("HI!")


# In[4]:


num=1.5
print(type(num))


# In[8]:


#type  brackets    ordered  mutable  duplicates            use 
#list  []          yes      yes      yes                   عام
#tuple ()          yes      no       yes                  الاحداثيات    
#set   {}          no       no       no                    العمليات الرياضية
#dict  {key:value} key      yes      nokeys , yes values   قواعد البيانات
x=[10,"ali",4.5,True] #list
print(x)
y=(1,2,1,6,3) #tuple
print(y)
z={1,4,5,6} #set
print(z)
person={"name":"shrouk","Age":20} #dict
print(person["name"])


# In[10]:


try:
    number=int(input("number: "))
    print(number)
except:
    print("invalid value")


# In[12]:


def hello():
    print("hello " + answer)

hello()


# In[15]:


n=int(input("n: "))
if n % 2 == 0:
    print("even")
else:
    print("odd")


# In[23]:


#Agree
s=input("DO YOU AGREE? ").lower()
if s in ["y","yes"] :
    print("Agreed!")
elif s in ["no","n"] :
    print("Not Agreed!")


# In[24]:


scores=[]
for i in range (3):
    score = int(input("score: "))
    scores.append(score)
print(f"Average{sum(scores)/len(scores)}")


# In[25]:


before=input("before: ")
print(f"after:{before.upper()}")


# In[27]:


import sys 
print(sys.version)
print(sys.platform)


# In[33]:


import sys
n= [1,2,3,4,5,0]
if 0 in n:
    print("Found")
    sys.exit(0)
print("Not Found")
sys.exit(1)


# In[ ]:




