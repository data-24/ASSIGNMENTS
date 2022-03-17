#!/usr/bin/env python
# coding: utf-8

# ### 1. Write a Python program to print 'Hello Pyhton'

# In[ ]:


print('Hello Python')


# ### Write a Python program to do arithmetical operations addition and division.?

# In[ ]:


import logging
logging.basicConfig(filename='operation.log',level=logging.DEBUG)
def opre(a,b):
    '''Write a Python program to generate a random number?'''
    logging.info('this starting of a program')
    try:
        a=int(input('enter the first number'))
        b=int(input('enter the second number'))
        logging.info('you have entered a and b values')
        c=int(input('enter 1 for addition or 2 for division'))
        if c==1:
            r=a+b
        else:
            r=a/b
        logging.info(r)
    except Exception as e:
        loggingG.error('you are in in exception block')
        loggigng.exception('enter correct value',+str(e))


# In[ ]:


opre(5,6)


# ### Write a Python program to find the area of a triangle?

# In[ ]:


import logging
logging.basicConfig(filename='area1.log',level=logging.DEBUG)
def tran(a,b,c):
    ''' Python program to find the area of a triangle'''
    try:
        logging.info('strating of a program')
        a = float(input('Enter first side: '))
        b = float(input('Enter second side: '))
        c = float(input('Enter third side: '))

        # calculate the semi-perimeter
        s = (a + b + c) / 2

        # calculate the area
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        logging.info(area)
    except Exception as e:
        logging.error('you are in exception block')
        logging.exception(e)
            


# In[4]:


tran(5,6,7)


# ### Write a Python program to swap two variables?

# In[7]:


def swap(a,b):
    c=0
    c=a
    a=b
    b=c
    return(a,b)
    


# In[8]:


swap(4,5)


# ### Write a Python program to generate a random number?

# In[13]:


import random
print(random.randint(4,50))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




