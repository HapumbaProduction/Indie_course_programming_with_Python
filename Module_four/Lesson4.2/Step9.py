word = input()
index = 0

while index < len(word):
    if word[index] == 'e' or word[index] == 'a':
        print('Ага! Нашлась')
        break
    else:
        print(f'Текущая буква: {word[index]}')
        index += 1
else:
    print('Распечатали все буквы')
