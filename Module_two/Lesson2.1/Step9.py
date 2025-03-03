characters = [input() for _ in range(3)]

print(*[characters.pop() for _ in range(3)], sep='\n')
