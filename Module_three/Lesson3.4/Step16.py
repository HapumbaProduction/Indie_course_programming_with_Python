s, v1, v2, t1, t2 = map(int, input().split())

time_first = 2 * t1 + s * v1

time_second = 2 * t2 + s * v2

if time_first < time_second:
    print("First")
elif time_first > time_second:
    print("Second")
else:
    print("Friendship")
