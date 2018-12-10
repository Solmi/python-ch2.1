a = 1.2
print(a, type(a))
print(isinstance(a, float))

b = 2.0
print(b, type(b))

# 객체 함수 is_integer()는 값이 정수인지 실수있지 확인하는 함수. 타입을 확인하는 함수가 아님
print(b.is_integer())