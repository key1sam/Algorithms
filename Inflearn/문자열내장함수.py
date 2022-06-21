msg = "It is Time"

#msg를 대문자로 출력해보기. upper()
print(msg.upper())

#msg를 소문자로 출력해보기. lower()
print(msg.lower())

#원하는 문자의 위치를 찾기
'''find 함수의 경우 다음과 같다.
1. string.find(찾을 문자)
2. string.find(찾을 문자, 시작 Index) // 어디서부터 탐색할지 지정
3. string.find(찾을 문자, 시작 Index, (끝 Index) // 어디서 탐색 종료할지 지정
찾는 문자(열)이 여러개 존재할 경우 더 앞쪽 인덱스를 반환하며 
존재하지 않을 시 -1을 반환한다.
'''
print(msg.find('T')) # 6 출력
print(msg.find('is')) #3 출력

#문자가 대문자일 경우 출력
for i in msg :
    if (i.isupper()) :
        print(i, end = '') #IT 출력
print() 

#문자가 소문자일 경우 출력
for i in msg :
    if (i.islower()) :
        print(i, end = '') #소문자 출력
print()

#문자가 알파벳인 경우 출력
for i in msg :
    if (i.isalpha()) :
        print(i, end = '')
print()


#문자의 아스키번호를 출력
a = 'A'
print(ord(a))

#정수를 아스키문자로 변경
b = 65
print(chr(b))

