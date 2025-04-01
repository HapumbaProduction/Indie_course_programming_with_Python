a, b = int(input()), int(input()) + 1
while a < b:
    if a == 777:
        break
    if a % 2 and a % 3:
        print(a)
    a += 1
