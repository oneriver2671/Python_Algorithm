'''
람다 함수
'''
def plus_one(x):
    return x+1

print(plus_one(1))

a = lambda x: x+2
print(a(1))

# 언제 유용한가? -> 내장함수의 인자로 사용될 때 편리
a = [1, 2, 3]

# map의 첫번째 인자 -> 함수명.
print(list(map(plus_one, a)))
print(list(map(lambda x: x+1, a)))

# sort 정렬할 때 람다 많이 사용


