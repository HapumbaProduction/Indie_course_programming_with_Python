if ((amount_guests := int(input())) == 2) or (amount_guests == 1):
    if amount_guests == 1:
        print(0)
    else:
        print(1)
else:
    if amount_guests % 2 == 0:
        print(int(amount_guests / 2))
    else:
        print(amount_guests)
