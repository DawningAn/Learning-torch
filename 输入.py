
name = input("请输入你の名字：")  # 以字符串的形式处理
print(name)

age = int(input("请输入你的年龄："))
print(age)

# eval1 = eval(input("请输入一个数："))
# print(eval1)
# print(type(eval1))

if age >= 18:
    print("你已经成年了！可以上网")
else:
    print("你还未成年，不能上网")