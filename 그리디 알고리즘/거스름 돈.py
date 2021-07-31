#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 가격을 입력받은 후 그리디 알고리즘을 활용하여 거스름돈의 개수 출력
num = int(input())

price = [500, 100, 50, 10]
count = [0 for _ in range(4)] # 500, 100, 50, 10원의 개수를 저장해준다.
count_index = 0

for i in price : # price 리스트 앞부터 순환
    count[count_index] = num // i # 가장 큰수로 나눈 몫을 count에 저장
    num -= i*count[count_index] # 앞의 price로 나눈 이후 남은 값을 표현
    count_index += 1 # 다음 금액의 개수를 저장하기 위해 이동

result = sum(count) # 동전 개수의 합 출력
print(result)

#시간 복잡도는 동전의 개수만큼 반복을 수행해야한다. 따라서 O(N)

