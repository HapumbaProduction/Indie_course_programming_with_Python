sentence = input("")

if sentence.endswith('.'):
    print("Законченное")
elif sentence.endswith(','):
    print("Незаконченное")
elif sentence.endswith('?'):
    print("Вопросительное")
elif sentence.endswith('!'):
    print("Восклицательное")
else:
    print("Неопределенное")
