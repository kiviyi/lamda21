a, b, c = [int(i) for i in input().split()]
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(c)