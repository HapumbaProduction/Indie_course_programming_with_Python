first_side, second_side, third_side = map(int, input().split())

print(((first_side + second_side) > third_side) and ((first_side + third_side) > second_side) and ((second_side + third_side) > first_side))
