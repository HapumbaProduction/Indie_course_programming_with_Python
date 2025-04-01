number = int(input())

if number > 0 and (number & (number - 1) == 0):
    amount_levels = 0
    while number > 1:
        number //= 2
        amount_levels += 1
    
    print(amount_levels)
else:
    print('НЕТ')
