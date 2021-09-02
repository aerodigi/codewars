def two_sort(array):
    my_string = ""
    array.sort()
    first_val = array[0]
    for i in first_val:
        my_string += i + "***"
    final_string = my_string[:-3]
    return final_string



























two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"])

# You will be given a vector of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

# The returned value must be a string, and have "***" between each of its letters.

# You should not remove or add elements from/to the array.
