import sys
sys.stdin=open("input.txt", "r")

'''
주사위 게임
'''
# 배열의 값들 중, 중복인 값의 개수 구하기

n = int(input())
result_arr = []

for i in range(n):
    arr = input().split()
    print(arr)

    # 정렬 (눈이 다 달랐을 땐 가장 큰 수를 찾아야 해서)
    arr.sort()
    a, b, c = map(int, arr)

    # 규칙1: 같은 눈 3개인 경우
    if a==b and b==c:
        money = 10000 + a*1000

    # 규칙2: 같은 눈 2개인 경우(1)
    elif a==b or a==c:
        money = 1000 + a*100

    # 규칙2: 같은 눈 2개인 경우(2)
    elif b==c:
        money = 1000 + b*100

    # 규칙3: 모두 다른 눈인 경우 (이 경우 때문에 정렬함)
    else:
        money = c*100
    

'''
아. 특별한 방법이 있던 것은 아니고, 내가 생각했던 방법이 맞구나.
if, elif문 태워서.
'''

    
    
