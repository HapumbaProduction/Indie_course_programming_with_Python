hours_1 = int(input())
minutes_1 = int(input())
seconds_1 = int(input())
hours_2 = int(input())
minutes_2 = int(input())
seconds_2 = int(input())

print(abs(((hours_1 * 60 * 60) + (minutes_1 * 60) + seconds_1) - ((hours_2 * 60 * 60) + (minutes_2 * 60) + seconds_2)))
