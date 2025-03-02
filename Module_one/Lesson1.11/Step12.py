import math

office_length, office_width, office_height = map(int, input().split())

print(math.ceil(((office_length * office_height + office_width * office_height) * 2) / 16))
