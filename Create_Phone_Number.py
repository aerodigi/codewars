def create_phone_number(n):
    full_list = []
    for x in n:
        full_list.append(x)
    p1 = full_list[0:3]
    p2 = full_list[3:]
    p1.insert(0,"(")
    p1.insert(4,")")
    p2.insert(3,"-")
    joined_list = p1 + p2
    print(joined_list)
    joined_list.insert(5," ")
    returned_number = ''.join(str(i) for i in joined_list)
    print(returned_number)


create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

# 0:2
