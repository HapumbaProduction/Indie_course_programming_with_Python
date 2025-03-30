string = input().strip()

print("Можно преобразовать" if (
    string.isdigit() or 
    (string.count('.') + string.count(',') <= 1 and 
    string.count(' ') == 0 and 
    not string.isalnum())
) else "Нельзя преобразовать")
