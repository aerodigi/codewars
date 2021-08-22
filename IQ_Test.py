def iq_test(list):
    numbers = list.split(" ")
    even_number_list = []
    odd_number_list =[]
    for i in numbers:
        i = int(i)
        if i % 2 == 0:
            even_number_list.append(i)
            print(even_number_list.index(i)+1)
        else:
            odd_number_list.append(i)
            # print(numbers.index(i))
            # return(numbers.index(oddInt)+1    
    on_length = len(odd_number_list)
    en_length = len(even_number_list)
    if on_length == 1:
        






iq_test('17 45 9 47 5 39 47 47 9 47 15 31 37 47 37 19 7 37 13 19 7 35 27 33 45 19 20 37 45 21 51 1 21 43')






# test.assert_equals(iq_test("2 4 7 8 10"),3)