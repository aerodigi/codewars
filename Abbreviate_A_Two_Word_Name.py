""" Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them."""

def abbrev_name(name):
    
    list_of_names = name.split(" ")
    surname_initial = list_of_names[1][0].capitalize()
    forename_initial = list_of_names[0][0].capitalize()
    dot_initials = forename_initial + "." + surname_initial
    return dot_initials
    


abbrev_name("ainsley gilligan")