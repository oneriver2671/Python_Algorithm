'''
정다면체
'''

from decimal import ROUND_HALF_UP
from operator import countOf
# import sys
# sys.stdin=open("input.txt", "rt")

'''
내 풀이
'''
# n, m = map(int, input().split())

# n_arr = list(range(1, n+1))
# m_arr = list(range(1, m+1))
# sum_arr = []

# for x in n_arr:
#     for y in m_arr:
#         sum_arr.append(x+y)


# sum_arr.sort()
# print(sum_arr)

# # 내장함수 max
# # 동일한 값인 경우, 첫번째 변수만 가져오네..
# max_count = max(sum_arr, key=sum_arr.count)
# print(max_count)


'''
내 풀이(2) - 정답 뜨긴 했는데 엄청 오래걸림. 문법 이것저것 찾아보면서 풀어서.
'''
# '합계 숫자'를 index로 두고. 그 합계 숫자가 나올 때마다, 값을 증가시키는 방식으로 풀이.
n, m = map(int, input().split())

n_arr = list(range(1, n+1))
m_arr = list(range(1, m+1))

# 사전 자료형 초기화 (2~(n+m)까지)
sum_dic = dict()  
for i in range(2, n+m+1):
    sum_dic[i] = 0

for x in n_arr:
    for y in m_arr:
        sum_dic[x+y] += 1


# key를 출력해야 함
maxVal = 0
for key, value in sum_dic.items():
    if maxVal < value:
        maxVal = value

# value가 maxVal인 것들의 key값을 출력.
result = []
for key, value in sum_dic.items():
    if value == maxVal:
        result.append(key)

result.sort()

for r in result:
    print(r, end=' ')



            

