number = int(input())
divisor = 2

while divisor <= number:
    if number % divisor == 0:
        print(divisor)
        break
    else:
        divisor += 1
