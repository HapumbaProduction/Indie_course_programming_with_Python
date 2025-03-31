num1 = float(input())
num2 = float(input())

operation = input()

if operation == '+':
    result = num1 + num2
    print(result)
elif operation == '-':
    result = num1 - num2
    print(result)
elif operation == '*':
    result = num1 * num2
    print(result)
elif operation == '/':
    if num2 == 0:
        print("Неизвестно")
    else:
        result = num1 / num2
        print(result)
else:
    print("Неизвестно")
