'''
리스트 내장함수
'''
import random as r

a = [1, 2, 3, 5, 4, 5]

a.append(5)       # list 뒤에 추가
a.insert(3, 7)    # index 3에 값 추가

print(a)


# 삭제 관련
removed_value = a.pop(3)     # index 3의 값 삭제, 반환
a.remove(5)    # 특정 value 삭제 (최초 1개만)

print(removed_value)


# remove All 구현
remove_set = {5}
new_list = [i for i in a if i not in remove_set]
print(new_list)

# 특정 값의 index를 반환
print(a.index(5))

# 계산
print(min(a))
print(min(10, 12))


