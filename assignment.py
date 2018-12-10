# 치환문 예
a = 1
b = a+1
print(a, b)
print(a, b, sep='____')

# 변수값 할당 오류
# 1 + a = c

# ;를 사용하는 예시(한줄에 나타내고싶을때)
e = 3.5; f = 5.3
print(e, f)

# 여러 개를 한 번에 할당할 때(추천)
e, f = 3.5, 5.3
print(e, f)

# 같은 값을 여러변수에 할당할 때
x = y = z = 10
print(x, y, z)

# c 스타일은 지원하지 않음
# x = ( y = 10)

# temp 안쓰고 변수 치환
print(e, f)
e, f = f, e
print(e, f)

# 동적타이핑: 변수에 새로운 값(타입)이 할당되면 기존의 값(타입)을 버리고 새로운 값으로 치환됨
a = 1
print(a, type(a))
a = "hello"
print(a, type(a))

# 확장 치환문
a = 10
a += 10
print(a)

a -= 3
print(a)



