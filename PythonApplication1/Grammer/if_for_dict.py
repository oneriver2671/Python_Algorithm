
'''
조건문
'''
score = int(input('점수 입력: '))
print(type(score))

if 70 < score < 80:
    result = "C등급"
elif 80 <= score < 90:
    result = "B등급"
elif score >= 90:
    result = "A등급"
else:
    result = "과락"

print(result)


'''
반복문 (for, while)
range() 내장함수
'''

## range()
# for(int i=0; i<=9; i++) 문법과 동일
a = range(10)   #순차적으로 정수 List를 만든다. (0~9)
print('a:', list(a))

# 홀수만 포함하는 배열
array = [i for i in range(20) if i%2 == 1]   
print(array)

# 짝수만 포함하는 배열
array2 = [j for j in range(20) if j%2 == 0]
print(array2)

# 1부터 N까지 홀수 출력하기
n = int(input('숫자 입력: '))

# 1번 case
for i in range(1, n+1):
    if i%2==1:
        print(i)

# 2번 case
array3 = [i for i in range(n) if i%2 == 1]  # i가 홀수면.
print(array3)

# 1부터 N까지의 합 구하기
sum = 0
for i in range(1, n+1):
    sum += i

print(sum)


# N의 약수 출력하기 (나머지가 0이면 약수)

for i in range(1, n+1):
    if n%i == 0:
        print(i, end=' ')   # 줄바꿈 없이, 옆으로 출력되도록.


'''
자료형
'''
# 딕셔너리 (key, value)
dic01 = {'key1': 3, 'key2': 9}
key_list = list(dic01.keys())    # key data 추출
value_list = list(dic01.values())  # value data 추출

print('key 목록:', key_list)
print('value 목록:', value_list)

dic02 = {'key5': 4, 'key5': 5}
key_list_2 = list(dic02.keys())    # key data 추출
value_list_2 = list(dic02.values())  # value data 추출



#################

test_dic = {'test01': '테스트1', 'test02': '테스트2'}

key_list = list(test_dic.keys())
value_list = list(test_dic.values())

print(key_list)
print(value_list)

#################

testList = [i for i in range(1, 101) if i%2 == 1]
print(testList)

test_dic01 = {'test01': 01, 'test02': 02}
test_dic02 = {'test03': 03, 'test04': 04}














