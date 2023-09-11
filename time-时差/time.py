weiduA = int(input("请输入A点纬度(-180到180，东+西-):"))
if weiduA > 180:
    print("数值过大")
elif weiduA < -180:
    print("数值过小")
else:
    shiquA = weiduA // 15


weiduB = int(input("请输入B点纬度(-180到180，东+西-):"))
if weiduB > 180:
    print("数值过大")
elif weiduB < -180:
    print("数值过小")
else:
    shiquB = weiduB // 15


if shiquA > 0 and shiquB > 0:
    shiquC = shiquA + shiquB
elif shiquA > 0 and shiquB < 0:
    shiquC = shiquA - shiquB
elif shiquA < 0 and shiquB < 0:
    shiquC = shiquA + shiquB * -1
elif shiquA < 0 and shiquB > 0:
    shiquC = shiquB - shiquA


shijianA = int(input("请输入A点时间(只输入小时):"))
if shijianA > 24:
    print("数值过大")
elif shijianA < 0:
    print("数值过小")


if shiquC > 0:
    shijianB = shijianA + shiquC
else:
    shijianB = shijianA < shiquC

print(shijianB)
