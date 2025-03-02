first_side, second_side, third_side = map(int, input().split())

print((first_side ** 2 + second_side ** 2 == third_side ** 2) or (second_side ** 2 + third_side ** 2 == first_side ** 2) or (first_side ** 2 + third_side ** 2 == second_side ** 2))
