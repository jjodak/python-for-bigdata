'''
이름 : 조준혁
학과 : 인공지능소프트웨어학과
'''

#1 원의 면적 구하는 함수
'''
def caculate_area(radius):
    area = 3.14*radius**2
    return area
c_area = caculate_area(5.0)
print(c_area)
'''

#2 정렬
'''
def sort_num(n1,n2):
    if n1 <n2:
        return n1,n2
    else:
        return n2,n1

print(sort_num(110,210))
print(sort_num(2100,80))
'''

#3 계산기
'''
def calc(n1,n2):
    return n1 +n2, n1-n2,n1*n2,n1/n2

n1,n2=200,100
t1,t2,t3,t4=calc(n1,n2)
print(n1,'+',n2,'=',t1)
print(n1,'-',n2,'=',t2)
print(n1,'*',n2,'=',t3)
print(n1,'/',n2,'=',t4)
'''

#4 거북이 그리기 - 정사각형
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

square(100)
square(200)
square(300)
turtle.done()
'''

#5 주급 계산기
'''
def weeklyPay(rate, hour):
    if(hour>30):
        money = rate*30 + 1.5*rate*(hour-30)
    else:
        money = rate*hour
    return money

r = int(input("시급을 입력하시오: "))
h = int(input("근무 시간을 입력하시오: "))
print("주급은 " + str(weeklyPay(rate = r, hour = h)))
'''