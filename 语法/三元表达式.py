a = 1
b = 2

print(a if a > b else b)  # 根据条件 a > b 来决定打印 a 还是 b
# 如果 a 大于 b，则打印 a
# 如果 a 不大于 b，则打印 b

# 猜拳游戏
import random

player = int(input("请输入你的选择(石头(2)或剪刀(1)或布(3)): "))

computer = random.randint(1, 3)
print(f"电脑选择了{computer})")
print(f"你选择了{player}")

if player == computer:
    print("平局！再来")
if ((player == 1) and (computer == 3)) or ((player == 2) and (computer == 1)) or ((player == 3) and (computer == 2)):
    print("你赢了！")
elif (player == computer):
    print("平局！再来")
else:
    print("你输了！")
