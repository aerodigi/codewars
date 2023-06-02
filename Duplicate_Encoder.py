"""The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string,
or ")" if that character appears more than once in the original string. 
Ignore capitalization when determining if a character is a duplicate."""

def duplicate_encode(word):
    lower_word = word.lower()
    blank_list = []
    for l in lower_word:
        blank_list += l
    bracket_list = []    
    for x in blank_list:
        if lower_word.count(x) > 1:
            bracket_list.append(")")
        else:
            bracket_list.append("(")
    answer = "".join(bracket_list)
    return answer



duplicate_encode("px@IAqWMVh(Z)fIPebWf")