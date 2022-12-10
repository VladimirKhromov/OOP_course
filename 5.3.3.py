def input_int_numbers():
    lst = input().split()
    for i in lst:
        try:
            int(i)
        except ValueError:
            raise TypeError('все числа должны быть целыми')
    return " ".join(lst)


while True:
    try:
        i = input_int_numbers()
    except:
        continue
    else:
        break

print(i)
