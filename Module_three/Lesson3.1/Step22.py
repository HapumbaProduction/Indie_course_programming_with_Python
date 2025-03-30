cell1 = input().strip()
cell2 = input().strip()

column1 = ord(cell1[0]) - ord('a') + 1
row1 = int(cell1[1])
column2 = ord(cell2[0]) - ord('a') + 1
row2 = int(cell2[1])

if (column1 + row1) % 2 == (column2 + row2) % 2:
    print("YES")
else:
    print("NO")
