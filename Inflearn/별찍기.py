'''반복문은 조건과 초기값이 같아질 때 작업을 종료한다'''
# 1~5
for i in range(5) :
    for j in range(i+1) :
        print('*', end = ' ')
    print()

print()

for i in range(5) :
    for j in range(5-i) :
        print('*', end = ' ')
    print()