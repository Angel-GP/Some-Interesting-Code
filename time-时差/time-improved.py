def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("输入的不是有效的整数，请重新输入。")

weiduA = get_input("请输入A点纬度(-180到180，东+西-):")
if weiduA > 180:
    print("数值过大")
elif weiduA < -180:
    print("数值过小")
else:
    shiquA = weiduA // 15

weiduB = get_input("请输入B点纬度(-180到180，东+西-):")
if weiduB > 180:
    print("数值过大")
elif weiduB < -180:
    print("数值过小")
else:
    shiquB = weiduB // 15

print("两者间相差时区:",shiquB)

if shiquA > 0 and shiquB > 0:
    shiquC = shiquA + shiquB
else:
    shiquC = abs(shiquA) + abs(shiquB)

shijianA = get_input("请输入A点时间(只输入小时):")
if shijianA > 24:
    print("数值过大")
elif shijianA < 0:
    print("数值过小")

shijianB = shijianA + shiquC
print(shijianB)
