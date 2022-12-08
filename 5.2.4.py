a, b = input().split()
try:
    a, b = int(a), int(b)
except:
    try:
        a, b = float(a), float(b)
    except:
        pass
print(a + b)