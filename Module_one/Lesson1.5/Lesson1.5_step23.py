first_number = int(input())
second_number = int(input())
third_number = int(input())

first_option = first_number + second_number + third_number
second_option = first_number + second_number * third_number
third_option = (first_number + second_number) * third_number
fourth_option = first_number * second_number + third_number
fifth_option = first_number * (second_number + third_number)
sixth_option = first_number * second_number * third_number

print(max(first_option, second_option, third_option, fourth_option, fifth_option, sixth_option))

