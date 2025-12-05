'''
이름 : 조준혁
학과 : 인공지능소프트웨어
'''

#1. 과일이름 받고 좋아하는 과일 찾기
'''
fruits = []
name = input('좋아하는 과일의 이름을 입력하시오: ')
fruits.append(name)
name = input('좋아하는 과일의 이름을 입력하시오: ')
fruits.append(name)
name = input('좋아하는 과일의 이름을 입력하시오: ')
fruits.append(name)

name = input('과일의 이름을 입력하시오:')

if name in fruits:
    print('이 과일은 당신이 좋아하는 과일입니다.')
else:
    print('이 과일은 당신이 좋아하는 과일이 아닙니다.')
'''

#2. 도시 인구 자료
'''
population = ['Seoul', 9765, 'Busan', 3441, 'Incheon', 2654]
print('서울 인구 : ',population[1])
print('인천 인구 : ',population[-1])

cities = population[::2]
print('도시 리스트 : ', cities)

pops = population[1::2]
print('인구의 합 : ', sum(pops))
 '''

#3. pop()
'''
lst = [0,10,20,30,40,50]
lst5 = lst.pop()
print(lst5,lst)
lst1=lst.pop(1)
print(lst1,lst)
'''

#4. sort(),reverse
'''
numbers = [9,6,7,1,8,4,5,3,2]
numbers.sort()
print(numbers) #[1,2,3,4,5,6,7,8,9]
numbers.sort(reverse=True)
print(numbers) #[9,8,7,6,5,4,3,2,1]
'''

#5. numbers sorted
'''
numbers = [9,6,7,1,8,4,5,3,2]
new_list = sorted(numbers)
print(new_list)
print(numbers)
'''

#6. list(), 인덱싱, 슬라이싱, split()
'''
s = 'python'
str_list = list(s)
print(str_list)

s = 'python'
print('s[0]=', s[0])
print('s[1]=', s[1])
print('s[-1]=', s[-1])
print('s[0:2]=', s[0:2])
print('s[-2:]=', s[-2:])
print('s[-1:-3:-1]=', s[-1:-3:-1])

s = '23 35 67 88 1'
num_list = s.split()
print(num_list)

s = '23,35,67,88,1'
num_list = s.split(',')
print(num_list)
'''

#7. 오늘의 명언
'''
import random

quotes = []
quotes.append('꿈을 지녀라. 그러면 어려운 현실을 이길 수 있다.')
quotes.append('언제나 현재에 집중 할 수 있다면 행복 할 것이다.')
quotes.append('고생없이 얻을 수 있는 진실로 귀중한 것은 하나도 없다.')
quotes.append('사람은 사랑할 때 누구나 시인이 된다.')
quotes.append('시작이 반이다.')

print("###############################")
print('#         오늘의 명언         #')
print("###############################")
print('')
dailyQuote = random.choice(quotes)
print(dailyQuote)
'''

#8. 최대 최소 구하기
'''
height = [178,173,166,164,176]
height.sort()
print('이 중에서 가장 작은 값은 : ', height[0])
print('이 중에서 가장 큰 값은 : ', height[-1])
'''

#9. min(), max()
'''
height = [178,173,166,164,176]
height.sort()
print('이 중에서 가장 작은 값은 : ', min(height))
print('이 중에서 가장 큰 값은 : ', max(height))
'''