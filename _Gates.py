#!/usr/bin/env python
# coding: utf-8

# In[35]:


def Not(A):
    w1=1
    op=0
    if(w1*A<0.5):
        op=1
    else:
        op=0
    return op
print(Not(1))
print(Not(0))


# In[36]:


def And(A,B):
    if A>1:
        A=1
    if(B>1):
        B=1
    op=0
    w1=w2=1
    E=w1*A+w2*B
    if(E>1.5):
        op=1
    else:
        op=0
    return op
print(And(132,54))


# In[37]:


def Or(A,B):
    if A>1:
        A=1
    if(B>1):
        B=1
    op=0
    w1=w2=1
    E=w1*A+w2*B
    if(E>0.5):
        op=1
    else:
        op=0
    return op
Or(0,0)


# In[38]:


def Nand(A,B):
    and_output=And(A,B)
    Not(and_output)
Nand(0,0)


# In[39]:


def Nor(A,B):
    or_output=Or(A,B)
    Not(or_output)
Nor(1,1)


# In[40]:


def Xor(A,B):
    w1=w2=1
    E=w1*A+w2*B
    if(E>0.5 and E<1.5):
        return 1
    return 0
print(Xor(1,0))


# In[41]:


def inot(A):
    return ~A+2
inot(1)


# In[42]:


def Xnor(A,B):
    return Not(Xor(A,B))
print(Xnor(0,0))


# In[43]:


def BiasAnd(A,B):
    w1=w2=1
    Bias=1.5
    E=(w1*A+w2*B)-Bias
    if(E>0):
        return 1
    return 0
BiasAnd(1,1)

