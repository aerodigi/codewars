''' Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. 
You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. 
Be careful, there shouldn't be a space at the beginning or the end of the sentence!'''


def smash(words):
    string = ""
    if len(words) == 0:
        return []
    else:
        for x in words[:-1]:
            string += x + " "
        for x in words[-1:]:
            string += x
        return string

        


smash(['hello', 'world', 'this', 'is', 'great'])