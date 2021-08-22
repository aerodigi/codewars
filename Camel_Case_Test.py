cc_tail_capitalized = cc_capitalized = camel_case_string = ""

def to_camel_case(text):
    if text == "":
        print(text + "An empty string was provided!")
        return text
    else:
        ccs_amended = text.replace("_", " ").replace("-", " ")
        ccs_amended_first_char = ccs_amended[0][0]
        if ccs_amended_first_char.isupper():
            ccs_first_char_is_upper(ccs_amended, ccs_amended_first_char, cc_capitalized)
        else:
            ccs_first_char_is_lower(ccs_amended, ccs_amended_first_char, camel_case_string)

def ccs_first_char_is_upper(ccs_amended, ccs_amended_first_char, cc_capitalized):
    if ccs_amended_first_char.isupper():
        cc_amended_list = ccs_amended.split(" ")
        for i in cc_amended_list:
            cc_capitalized += i.capitalize() + " "
            camel_case_string = cc_capitalized.replace(" ", "")
        print(camel_case_string)
        return camel_case_string

def ccs_first_char_is_lower(ccs_amended, cc_tail_capitalized, camel_case_string):
    cc_amended_list = ccs_amended.split(" ")
    cc_amended_list_first_item = [cc_amended_list[0]]
    cc_amended_list_tail_items = cc_amended_list[1:]
    for i in cc_amended_list_tail_items:
        cc_tail_capitalized += i.capitalize() + " "
        cc_tail_capitalized_list = cc_tail_capitalized.split(" ")
        cc_joined_list = cc_amended_list_first_item + cc_tail_capitalized_list
        cc_joined_list.remove(cc_joined_list[-1])
    camel_case_string = camel_case_string.join(cc_joined_list)
    print(camel_case_string)
    return camel_case_string

    
to_camel_case("")