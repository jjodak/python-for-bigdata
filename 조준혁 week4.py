'''
이름 : 조준혁
학과 : 인공지능소프트웨어학과
'''

#1. if
'''
x = 100
if x>1:
    print("x는 1보다 큽니다.")
'''

#2. if-else
'''
score=int(input("점수를 입력하세요."))

if score >=60:
    print("합격입니다.")
    print("장학금도 수령하세요.")
else:
    print("불합격입니다.")
'''

#3. 홀짝 판단
'''
num=int(input("양의 정수를 입력하시오 : "))
if num%2 == 0:
    print("짝수 입니다.")
else:
    print("홀수 입니다.")
'''

#4. 양수음수 + 홀짝 판단
'''
num = int(input("정수를 입력하시오 : "))

if num >= 0:
    print("양수입니다.")
    if num % 2 == 0:
        print("짝수 입니다.")
    else:
        print("홀수 입니다.")
else:
    print("음수입니다.")
'''

#5. 영화
'''
age = int(input("나이를 입력하시오 : "))

if age >= 15:
    print("본 영화를 보실 수 있습니다.")
else:
    print("본 영화를 보실 수 없습니다.")
'''

#6. 동전던지기 게임
'''
import random

print("동전 던지기 게임을 시작합니다.")
coin = random.randrange(2)

if coin == 0:
    print("앞면입니다.")
else:
    print("뒷면입니다.")
print("게임이 종료되었습니다.")
'''

#7. elif
'''
num = int(input("정수를 입력하시오 : "))

if num > 0:
    print("양수입니다.")
elif num == 0:
    print("0 입니다.")
else:
    print("음수입니다.")
'''

#8. 중첩 if
'''
num = int(input("정수를 입력하시오 : "))

if num >= 0:
    if num == 0:
        print("0 입니다.")
    else:
        print("양수입니다.")
else:
    print("음수입니다.")
'''

#9. 로그인
'''
id = "ilovepython"
pw = "qwer1234"

s = input("아이디를 입력하시오 : ")
s2 = input("비밀번호를 입력하시오 : ")
if s == id:
    if s2 == pw:
        print("환영합니다.")
    else:
        print("비밀번호가 올바르지 않습니다.")
else:
    print("아이디를 찾을 수 없습니다.")
'''

#10. 복붙
'''
print("파이썬 주식회사의 방문을 환영합니다!")
print("파이썬 주식회사의 방문을 환영합니다!")
print("파이썬 주식회사의 방문을 환영합니다!")
print("파이썬 주식회사의 방문을 환영합니다!")
print("파이썬 주식회사의 방문을 환영합니다!")
'''

#11. for
'''
for i in range(100):
    print(i, "파이썬 주식회사의 방문을 환영합니다!")
'''

#12. for - list
'''
for i in [1,2,3,4,5]:
    print("방문을 환영합니다!")
'''
#13. for - list
for i in [1,2,3,4,5]:
    print("i = ",i)