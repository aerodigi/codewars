def split_uppercase(s):
    r = []
    l = False
    for c in s: #for character in string
        # l being: last character was not uppercase
        if l and c.isupper(): #if last character is not uppercase
            r.append(' ') #append a space to the end of 
            print(r)
        l = not c.isupper() #if last character 
        print(l)
        r.append(c)
        result = ''.join(r)
    print(result)


split_uppercase("AshleyPlane")

        
l = False
c[0] = "A"
l = True
c[1] = "s"


# from typing import Counter


# def to_underscore(string):
#     upper_case_index = []
#     lower_case_index_count = []
#     new_string = []
#     for i in string:
#         if i.isupper():
#             upper_case_index.append(string.index(i))
#     print(upper_case_index)
#     for n in upper_case_index:
#         new_string.append(string[n])
#     print(new_string)
#     for i in new_string:
#         if i in string:
#             split_string = string.rsplit(i)
#     print(split_string)
        #     print(updated_string)
    #         upper_case_index_count.append(upper_case_index)
    #         new_string = string.split(" ",upper_case_index)
    #         print(new_string)
    #     else:
    #         lower_case_index = string.index(i)
    #         lower_case_index_count.append(lower_case_index)

    # print(len(upper_case_index_count))
    # print(len(lower_case_index_count))
    # print(len(string))
            # print(type(upper_case_index))
            # print(type(upper_case_index_count))
            

        # else:
        #     lower_index = string.index(i)
        #     print(lower_index)

        
# AshleyPlane


# to_underscore("AshleyPlaneSmells")






''' Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation.
Lowercase characters can be numbers. If the method gets a number as input, it should return a string.
Examples

"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"

'''