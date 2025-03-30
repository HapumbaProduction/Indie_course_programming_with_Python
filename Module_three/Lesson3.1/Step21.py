N = input().zfill(6)

first_half_sum = int(N[0]) + int(N[1]) + int(N[2])
second_half_sum = int(N[3]) + int(N[4]) + int(N[5])

if first_half_sum == second_half_sum:
    print("YES")
else:
    print("NO")
