status = ['Fizz', 'Buzz', 'FizzBuzz']

if ((value := int(input())) % 3 == 0 and value % 5 != 0):
    print(status[0])
elif (value % 5 == 0 and value % 3 != 0):
    print(status[1])
elif (value % 3 == 0 and value % 5 == 0):
    print(status[2])
else:
    print(value)
