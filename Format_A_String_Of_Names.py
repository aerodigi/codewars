def namelist(names):
    mylist = list(names)
    test_list = []

    for x in mylist:
        test_list += list(x.values())
    

    if len(test_list) < 2:
        seperator = ""
        one_word_list = seperator.join(test_list)
        print(one_word_list)
        return one_word_list

    elif len(test_list) < 3:
        seperator_three = "&"
        two_word_list = seperator_three.join(test_list)
        print(two_word_list)
        return two_word_list


    else:
        test_list.insert(-1, " &")
        seperated_list_one = test_list[0:-2]
        seperator_one = ", "
        my_seperated_string_one = seperator_one.join(seperated_list_one) 

        seperated_list_two = test_list[-2:]
        seperator_two = " "
        my_seperated_string_two = seperator_two.join(seperated_list_two)

        final_string = my_seperated_string_one + my_seperated_string_two
        print(final_string)
        return final_string




    # my_final_string = my_string + test_list_two

    # print(my_final_string) 

    # if len(test_list) > 2:
    #     my_string = ", ".join(test_list)

    # print(my_string)

    # my_string = ", ".join(test_list)
    # new_list = list(my_string)
    # print(new_list)
    #print(my_string)
    # updated_string = list(my_string)
    # print(updated_string)
    # second_updated_string = ''.join(updated_string)

    # print(second_updated_string)

    # print(type(my_string))
    # updated_string = my_string.replace("&,", "&")
    # print(updated_string)
    # updated_string = my_string.replace(", ", " ", -2)
    # print(updated_string)
    # my_seperator = " "
    # empty_string = my_seperator.join(test_list)
    # print(empty_string)


namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])