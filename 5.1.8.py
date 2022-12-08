lst_in = "1 -5.6 2 abc 0 False 22.5 hello world".split()



def get_number(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x

lst_out = list(map(get_number, lst_in))
print(lst_out)