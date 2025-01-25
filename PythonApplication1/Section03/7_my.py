import sys
sys.stdin=open("input.txt", "r")

'''
소수 (에라토스테네스 체)
'''

'''
내 풀이
'''
# 1과 자기 자신만 약수로 가짐
n=int(input())
arr=[i for i in range(1, n+1)]
result_arr = []
   
for x in arr:
    tmp=[]
    for i in range(1, x+1):
        if x%i==0:
            tmp.append(i)

        if len(tmp)==2 and tmp[1]==x:   # 이거 좀 더 줄이고 싶음.
            result_arr.append(x)

print(len(result_arr))

'''
new 풀이 
'''



