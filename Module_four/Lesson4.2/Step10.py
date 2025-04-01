numbers = list(map(int, input().split()))
target_sum = int(input())
final_sum = 0
index = 0

while index < len(numbers):
    final_sum += numbers[index]
    index += 1
    if final_sum >= target_sum:
        print(final_sum)
        print('Цель достигнута')
        break
else:
    print(final_sum)
    print('Цель не достигнута')
