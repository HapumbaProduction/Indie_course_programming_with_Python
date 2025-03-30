if (first_string := input().lower()) == (second_string := input().lower()):
    print(0)
else:
    if first_string < second_string:
        print(-1)
    else:
        print(1)
