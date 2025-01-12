

'''
문자열과 내장함수
'''

msg = "It is time"
print(msg.upper())   # 대문자로 만드는 함수
print(msg.lower())   # 소문자로 만드는 함수

tmp = msg.upper()

print(tmp.find('T'))  # 문자열 찾기 (인덱스 번호를 반환)
print(tmp.count('T')) # 문자열 개수 반환

# 슬라이스
print(msg)      # - 결과: "It is time"
print(msg[:2])  # 0~1번 index까지의 문자열 출력 - 결과: "It"
print(msg[3:5]) # 3~4번 index까지의 문자열 출력 - 결과: "is"


msg = "gogo"
print(msg)

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

testMsg = "Justin"

print(testMsg[:2])
print(testMsg[2:5]) 
print('길이:', len(testMsg))

for i in range(len(testMsg)):
    print(testMsg[i])


testMessage = 'Hello, My Name is Oneriver'

for i in range(len(testMessage)):
    print(testMessage[i])



'''
아스키 넘버 (유니코드)
A: 65, Z: 90
a: 97, z: 122
'''
# ord(): 아스키 넘버를 출력하는 함수
tmp = 'AZ' 
for x in tmp:
    print(ord(x))    # 결과: 65 90
   
tmp = 'az'
for x in tmp:
    print(ord(x))    # 결과: 97 122

# chr(): 아스키 넘버를 문자열로 출력 (65->A)
tmp = 65
print(chr(tmp))      # 결과: A




   


    









 