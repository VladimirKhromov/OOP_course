lst_in = "1 -5.6 2 abc 0 False 22.5 hello world".split()



def filter_srt_to_int(st):
    try:
        int(st)
    except ValueError:
        return False
    return True

print(sum(map(int, (filter(filter_srt_to_int, lst_in)))))