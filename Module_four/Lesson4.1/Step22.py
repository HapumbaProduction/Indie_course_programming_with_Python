number = input()

while int(number[0]) != 1 and int(number) < 10 ** 9:
    number = int(number[0]) * int(number)
    number = str(number)
print(number)
