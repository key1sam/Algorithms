#!/usr/bin/env python
# coding: utf-8

# In[16]:


a, b = map(int, input().split())

# num1, num2의 최대공약수는 num2와 (num1 % num2)의 최대 공약수와 동일하다.
# 그러다가 나머지가 0이 되는 지점에서 더 작은 수가 최대 공약수가 된다.

def GCD(num1, num2) :
    if num1 % num2 == 0 :
        print(num2)
    else :
        GCD(num2, (num1%num2))
            
GCD(a, b)

