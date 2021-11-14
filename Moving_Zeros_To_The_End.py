def move_zeros(array):
    non_zero_list = [i for i in array if i != 0]
    zero_list = [i for i in array if i == 0]
    array = non_zero_list + zero_list
    print(array)
    return array


move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])