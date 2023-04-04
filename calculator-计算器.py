# 定义一个函数，接收两个参数和一个操作符，返回计算结果
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"

# 获取用户输入的数字和操作符
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# 调用计算器函数并输出结果
result = calculator(num1, num2, operator)
print("Result: ", result)
input("Press Enter to exit...")