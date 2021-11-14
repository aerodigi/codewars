# Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If the method gets a number as input, it should return a string.
# Examples

# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7Test"        -->  "app7_test"
# 1                 -->  "1"

def to_underscore(string):
    upper_case = []
    string_len = len(string)
    print(string_len)
    for x in string:
        if x.isupper():
            upper_case += x
        if upper_case[1]in string:
            second_index = string.index(x)
    print(second_index)
    print(upper_case)
            

    # print(type(string))
    # myString = ""
    # for i in string:
    #     if .istitle(i)
    # for i in string:
        
    # myList = []
    # for i in string:
    #     myList += i
    # for j in myList:
        
    
        
            


to_underscore("TestController")

#psuedocode
#


# find index of 