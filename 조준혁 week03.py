'''
이름 : 조준혁
학과 : 인공지능소프트웨어학과
'''

#1. 입력받아 나머지와 몫 구하기
'''
p = int(input("분자를 입력하시오: "))
q = int(input("분모를 입력하시오: "))

print("나눗셈의 몫: ", p//q)
print("나눗셈의 나머지: ", p%q)
'''

#2. 원리금 합계 복리 계산기
'''
a = 1000
r = 0.05
n = 10

print("원리금 합계: ", a*(1+r)**n)
'''

#3. 화씨 -> 섭씨
'''
f = float(input("화씨 온도를 입력하시오: "))
c = (f - 32) * (5/9)

print("화씨 온도 : ", f)
print(f"섭씨 온도 : {c:.2f}")
'''

#4. 평균값 구하기
'''
x = int(input("첫 번째 수를 입력하시오: "))
y = int(input("두 번째 수를 입력하시오: "))
z = int(input("세 번째 수를 입력하시오: "))

avg = (x+y+z) / 3
print("평균 = ", avg)
'''

#5. random모듈
'''
import random
x = random.random()
print(x)

x = random.random()
print(x)

x = random.randint(1,7)
print(x)

x = random.randrange(7)
print(x)

x = random.randrange(1,7)
print(x)

x = random.randrange(0,10, 2)
print(x)

lst = [10, 20, 30, 40, 50]
random.shuffle(lst)
print(lst)

print(random.choice(lst))
'''

#6. math모듈
import math
print(math.pow(3,3))
print(math.fabs(-99))
print(math.log(2.71828))
print(math.log(100,10))
print(math.pi)
print(math.sin(math.pi/2.0))
      

