
'''
리스트와 내장함수(2)
'''

a = [32, 17, 15, 23, 5]

# 슬라이스
print(a[:3])
print(a[1:4])

print(len(a))   # 리스트 길이


# 방식 1
for i in range(len(a)):
    print(a[i], end=' ')

# 방식 2 (forEach와 비슷)
for x in a:
    print(x, end=' ')
print()
 
# enumerate -> 튜플 형태로 출력. (index, value)
for x in enumerate(a):
    print(x)
print()

for index, value in enumerate(a):
    print(index, value)
print()


# all -> 모두가 참이면
if all(3<x<35 for x in a):
    print("Yes")
else:
    print("No")


# any -> 아무거나 하나라도 참이면
if any(x<15 for x in a):
    print("Yes")
else:
    print("No")



