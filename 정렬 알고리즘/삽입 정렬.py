#!/usr/bin/env python
# coding: utf-8

# ### 삽입 정렬
# - 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입합니다.
# - 시간복잡도는 최악의 경우 O(N^2)이며 최선의 경우 O(N)의 결과를 얻게된다.

# In[3]:


# 8월 15일 제작
num = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(num)) : # 1번 인덱스부터 앞쪽에 자기 자리를 찾아가기 위해 지정했다. (삽입 정렬)
    will_sort_index = i # 자신의 자리를 찾아가고는 수의 인덱스를 가리킨다. 
    for j in range(i-1, -1, -1) : # 처음에 sort될 인덱스의 바로 앞자리부터 0번째 인덱스까지 자리를 탐색하기 위해 for문을 다음과 같이 구성
        if num[j] > num[will_sort_index] :
            num[j], num[will_sort_index] = num[will_sort_index], num[j]
            will_sort_index = j
        else :
            break
            
print(num)

'''break구문을 생각했었으나 혹시 모를 예외가 발생하지 않을까라는 생각에 모든 인덱스를 탐색하게 되면서
비효율적인 구문이 탄생했었다. 또한 will_sort_index를 두지 않을 수 있었다.'''


# In[1]:


# 8월 17일 제작
num = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(num)) :
    for j in range(i, 0, -1) : # 위의 코드에서는 will_sort_index를 가지고 정렬될 값을 지정해주었으나
        if num[j] < num[j-1] : # for문의 변경값을 통해 정렬될 값도 통제할 수 있었다.
            num[j], num[j-1] = num[j-1], num[j]
        else : 
            break # 앞쪽은 정렬이 진행되어 있으므로 순서가 맞을 경우 break 수행할 수 있다.
print(num)


# In[ ]:




