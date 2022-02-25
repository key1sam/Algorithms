#!/usr/bin/env python
# coding: utf-8

# In[2]:


#퀵 정렬
''' 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나입니다.
병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정합니다.
퀵 정렬은 평균으 경우 O(NlogN)의 시간 복잡도를 가집니다.
하지만 최악의 경우 O(N^2)의 시간 복잡도를 가집니다. (이미 정렬된 리스트의 경우)'''


num = [7, 1, 4, 2, 5, 3, 6, 9, 8]

def quicksort(num, start, end) :
    if start >= end :
        return
    pivot = start # 처음 인덱스를 pivot으로 지정
    left = start + 1
    right = end
    while (left <= right) : # 엇갈릴 때까지 수행하기
        while (left <= end and num[pivot] >= num[left]) : # pivot보다 큰 값이 나올때 까지 진행한다.
            left += 1
        while (right > start and num[pivot] <= num[right]) : # right >= start로 해서 오류가 처음에 발생. 인덱스가 -1번째가 되어서 오류
            right -= 1
        if (left > right) :
            num[pivot], num[right] = num[right], num[pivot] # swap이 이루어지더라도 값이 바뀌는거지 pivot, right 인덱스 위치 자체는 바뀌지 않는다.
        else :
            num[left], num[right] = num[right], num[left]
    quicksort(num, start, right-1)
    quicksort(num, right+1, end)
    
quicksort(num, 0, len(num)-1)
print(num)


# In[3]:


a = 5
print(a)


# In[ ]:




