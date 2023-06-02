'''Take 2 strings s1 and s2 including only letters from a to z. 
Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.'''


def longest(a1, a2):
    blank_list = []
    blank_list += a1 + a2
    sorted_set = set(blank_list)
    sorted_list = sorted(list(sorted_set))
    answer = "".join(sorted_list)
    print(answer)



longest("arehtheyhere", "yestheyare")
longest("loopingisfunbutdangerous", "lessdangerousthancoding")
longest("inmanylanguages", "theresapairoffunctions")