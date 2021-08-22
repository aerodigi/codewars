def valid_parentheses(string):
    open = []
    close = []
    for x in string:
        if x == "(":
            open += x
        elif x == ")":
            close += x
    print(open)
    print(close)


valid_parentheses("()()))(((")

