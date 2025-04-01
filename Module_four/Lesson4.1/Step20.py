a, b = map(int, input().split())

hours = 0
burnt_out = 0

while a > 0:
    hours += a
    burnt_out += a
    a = burnt_out // b
    burnt_out = burnt_out % b

print(hours)
