'''
자릿수의 합
'''

from re import split
import sys
sys.stdin=open("input.txt", "rt")

'''
정답
str(x)까지는 생각했는데, 이걸 list에 넣으려고 해서 오류났던.
그냥 바로 for문 돌리면 되는구나.
'''

n = int(input())
a = map(int, input().split())

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

max = -2147000000

for x in a:
    tot = digit_sum(x)
    # tot 중 가장 큰 값 찾기
    if tot > max:
        max = tot 
        result = x
    
print(result)
    
