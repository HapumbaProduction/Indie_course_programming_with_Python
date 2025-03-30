string = len(input())

if string % 2 == 0:
    if string < 6:
        print('четная короткая')
    else:
        print('четная большая')
else:
    if string < 6:
        print('нечетная короткая')
    else:
        print('нечетная большая')
