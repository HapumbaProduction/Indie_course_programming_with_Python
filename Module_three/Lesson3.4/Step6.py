if (first_number := int(input())) == (second_number := int(input())):
    print('=')
else:
    if first_number < second_number:
        print('<')
    else:
        print('>')
