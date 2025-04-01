number = int(input())
number_for_square = 1
square = 0

while square < number:
    square = number_for_square ** 2
    number_for_square += 1
    if square <= number:
        print(square)
