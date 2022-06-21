'''1) 1부터 N까지의 홀수 출력하기
int()는 정수문자열(interger string)과 실수만 인수로 받는다.
따라서 input()으로 실수문자열(float string)을 받을 경우 에러가 발생한다.'''
N = int(input())
for i in range(1, N+1) :
    print(i, end = ' ')    
print("1번 정답 출력 완료")

'''2) 1부터 N까지의 합을 구하기'''
sum = 0
for i in range(1, N+1) :
    sum = sum + i
print(sum, end = ' ')
print("2번 정답 출력 완료")


'''3) N의 약수 출력하기'''
answer = []
for i in range(1, N+1) :
    if (N%i == 0) :
        answer.append(i)
for i in answer :
    print(i, end = ' ')
print("3번 정답 출력 완료")
