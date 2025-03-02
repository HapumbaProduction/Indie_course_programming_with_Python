n = int(input())

count_100 = n // 100
n %= 100

count_20 = n // 20
n %= 20

count_10 = n // 10
n %= 10

count_5 = n // 5
n %= 5

count_1 = n // 1

total_count = count_100 + count_20 + count_10 + count_5 + count_1

print(total_count)
