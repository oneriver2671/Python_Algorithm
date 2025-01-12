'''
함수 만들기
'''

def add(a, b):
    c = a + b
    return c

 
# 소수 판단하는 함수 -> 1과 자기 자신만 약수로 가짐 
def isPrime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True


# 리스트에서 소수인 값들만 출력하기
a = [12, 13, 7, 9, 19]

for y in a:
    if isPrime(y):
        print(y, end=' ')





