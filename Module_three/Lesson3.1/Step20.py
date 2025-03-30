a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    if a == b or a == c or b == c:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
