numbers = list(map(int, input().split()))

while 4 in numbers or 7 in numbers:
    if 4 in numbers:
        numbers.remove(4)
    if 7 in numbers:
        numbers.remove(7)

count_of_fives = numbers.count(5)

while count_of_fives < 10:
    numbers.append(5)
    count_of_fives += 1

print(numbers)
