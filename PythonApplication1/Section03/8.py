'''
뒤집은 소수 (복습 필요)
'''

import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))


# 뒤집는 함수 구현
def reverse(x):

    res = 0
    while x>0:
        t = x%10      # 10으로 나눈 것의 나머지 (1의 자리 숫자)
        res = res*10+t
        x = x//10     # 10으로 나눈 후의 몫

    return res


# 소수인지 확인하는 함수 구현
def isPrime(x):
    # 1 제외
    if x==1:
        return False

    # 소수가 아닌 값 찾기 -> 값의 절반까지만 돌면 된다. (2로 나누면 절반)
    for i in range(2, x//2+1):   
        if x%i==0:
            return False

    else:
        return True


for x in arr:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')






