



# 정수형으로 변경하기 -> map(int, ~ ) 사용.
a, b = map(int, input().split())   # 공백값 제거하면서, 배열 만들어준다. (split)
print(a+b)

data = list(map(int, input('숫자 입력: ').split()))
print(data)

checkData = [data[0]%2, data[1]%2, data[2]%2]   # 나머지 구하기 (홀수, 짝수 확인 시 많이 사용)

print(data.sort())
print(data.sort(reverse=True))


a, b = map(int, input('숫자 2개 입력: ').split())


print(int(a/b))   # 나누기 연산 (실수형으로 반환되어서 int()처리)
print(a//b)     # 몫
print(a**b)     # 거듭제곱


c = a/b

print(type(c))  # -> float 반환








