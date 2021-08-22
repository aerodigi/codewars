def to_camel_case(text):
    cc_tail_capitalized = cc_capitalized = camel_case_string = ""
    if text == "":
        return text
    else:
        ccs_amended = text.replace("_", " ").replace("-", " ")
        ccs_amended_first_char = ccs_amended[0][0]
        if ccs_amended_first_char.isupper():
            cc_amended_list = ccs_amended.split(" ")
            for i in cc_amended_list:
                cc_capitalized += i.capitalize() + " "
                camel_case_string = cc_capitalized.replace(" ", "")
            return camel_case_string
        elif ccs_amended_first_char.islower():
            cc_amended_list = ccs_amended.split(" ")
            cc_amended_list_first_item = [cc_amended_list[0]]
            cc_amended_list_tail_items = cc_amended_list[1:]
            for i in cc_amended_list_tail_items:
                cc_tail_capitalized += i.capitalize() + " "
                cc_tail_capitalized_list = cc_tail_capitalized.split(" ")
                cc_joined_list = cc_amended_list_first_item + cc_tail_capitalized_list
                cc_joined_list.remove(cc_joined_list[-1])
            camel_case_string = camel_case_string.join(cc_joined_list)
            return camel_case_string


""" 
Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized 
(known as Upper Camel Case, also often referred to as Pascal case).
Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior" 
"""
