#!/usr/bin/env python
# coding: utf-8

# ### 선택 정렬
# - 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 맞바꾸는 것을 의미한다.
# - 가장 작은 수를 전부 탐색해보고 앞으로 가져오는 형식이다.
# - N-1 + N-2 + N-3 + ... 2의 연산을 수행해야하므로 시간 복잡도는 O(N^2)이 나오게 된다.

# In[2]:


num = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(0, len(num)) : # 앞에서부터 정렬될 자리를 지정해준다.
    min_index = i # 정렬되지 않은 수에서 가장 앞자리
    for j in range(i+1, len(num)) :
        if num[min_index] > num[j] : 
            min_index = j # min_index보다 작은 값이 등장할 경우 
    num[min_index], num[i] = num[i], num[min_index] # 파이썬에서의 swap

print(num)

