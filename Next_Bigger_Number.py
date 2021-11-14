def next_bigger(n):
    my_string = ""
    lsn = list(str(n))
    lsn.sort(reverse=True)
    for i in lsn:
        my_string += i
    number_string = int(my_string)
    return number_string

next_bigger(12)