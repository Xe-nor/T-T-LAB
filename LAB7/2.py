def reverse_last_5(lst):
    if len(lst) < 5:
        return lst
    else:
        return lst[:-5] + lst[-5:][::-1]