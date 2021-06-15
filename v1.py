def valid_parentheses(string):
    new_list = list(string)
    open_bracket_count = 0
    closed_bracket_count = 0
    bracket_care_list = []
    
    for bracket in new_list:
        if bracket == "(":
            bracket_care_list += bracket
            open_bracket_count += 1
        elif bracket == ")":
            bracket_care_list += bracket
            closed_bracket_count += 1
        else:
            pass

    if new_list == []:
        print("True here")
        return True
    elif bracket_care_list[0::2][:] == ")" and bracket_care_list[1::2][:] == "(":
        print(bracket_care_list)
        print(bracket_care_list[::2][:])
        print(bracket_care_list[1::2][:])
        print(False)
        return False
    elif open_bracket_count == closed_bracket_count:
        print("True there")
        return True
    # else:
    #     print(False)
    #     return False



valid_parentheses("hi(hi)()")