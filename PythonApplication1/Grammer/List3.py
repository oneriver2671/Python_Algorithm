
'''
2차원 리스트 생성과 접근
'''

a = [0]*3   # 0이 3개 들어간 1차원 리스트가 생성됨


# 2차원 리스트 생성 방법
b = [[0]*3 for _ in range(3)]
print(b)

b[1][2] = 32
b[2][1] = 5

print(b)

# 2차원 리스트는 표로 접근하면 좋다.

for x in b:
    print(x)

for x in b:
    for y in x:
        print(y, end=' ')
    print()


