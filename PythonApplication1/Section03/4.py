'''
대표값 구하기
- 평균값과, 평균과 가장 가까운 값을 구하라.
'''

import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))

# sum_arr = 0
# for x in arr:
#     sum_arr += x

# 반올림 값 -> round()
avg = round(sum(arr)/n)    # list 안의 값들 모두 더하기 -> sum()
min = 2147000000

for idx, x in enumerate(arr):
    tmp = abs(x-avg)
    if tmp < min:
        min = tmp
        res = idx+1
        score = x
    # 차이가 같은 경우
    elif tmp == min:
        if x > score:
            score = x
            res = idx+1

print(avg, res)


# closed_val = float('inf')

# # 절대값 -> abs()
# # 정답 확인
# for x in arr:
#     if abs(avg-x) < closed_val:
#         closed_val = x

# print(avg, closed_val)   





            

