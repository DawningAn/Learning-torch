str = 'Hello, world!'

a = str.encode()  # 二进制字节流
print(type(str))

print(a)

b = a.decode()  # 将字节流解码为字符（还原为字符串）

print(b)