age_categories = ['Младенец', 'Малыш', 'Ребенок', 
                  'Подросток', 'Взрослый человек', 'Пожилой человек']

if (age := int(input())) < 2:
    print(age_categories[0])
elif 2 < age < 4:
    print(age_categories[1])
elif 4 <= age < 12:
    print(age_categories[2])
elif 12 <= age < 19:
    print(age_categories[3])
elif 19 <= age < 65:
    print(age_categories[4])
else:
    print(age_categories[5])
