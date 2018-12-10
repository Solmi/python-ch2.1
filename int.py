# 2진, 8진, 16진 Literal
a = 23
print(type(a))

b = 0b1101
o = 0o23
h = 0x23
print(b, o, h)

# 3.x에서는 int와 long이 합쳐짐. 표현범위 무한대
e = 2**1024
print(e, type(e))

# 변환 함수
print(oct(38))
print(hex(38))
print(bin(38))
