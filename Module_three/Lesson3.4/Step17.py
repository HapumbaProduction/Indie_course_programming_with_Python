first_string = input().strip()
second_string = input().strip()

last_char = first_string[-1]

if last_char == 'ь':
    if len(first_string) > 1:
        last_char = first_string[-2]
    else:
        last_char = ''

first_char = second_string[0] if second_string else ''

if last_char.lower() == first_char.lower():
    print("Good")
else:
    print("Bad")
