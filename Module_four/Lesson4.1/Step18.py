X, Y = map(int, input().split())
amount_days = 1

while X < Y:
    if X < Y:
        X *= 1.15
        amount_days += 1
    else:
        print(amount_days)

print(amount_days)
