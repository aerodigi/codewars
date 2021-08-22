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
        print("True1")
        return True
    elif bracket_care_list[0] == ")":
        print("False1")
        return False
    elif bracket_care_list[-1] == "(":
        print("False2")
        return False
    elif bracket_care_list[0::2][:] == ")" and bracket_care_list[1::2][:] == "(":
        print("False3")
        return False
    elif open_bracket_count == closed_bracket_count:
        print("True2")
        return True
    elif open_bracket_count != closed_bracket_count:
        print("False4")
        return(False)
    else:
        print("False5")
        return False
    

valid_parentheses("()))(()")




