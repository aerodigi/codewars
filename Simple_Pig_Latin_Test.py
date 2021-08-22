#create a list with each word in - Done.
#put individual words into list of lists - 
#count each word in the list
#take the first and last letters of each list 
#append "ay"

def pig_it(text):
    omit_chars = ['!','?']
    words = text.split(' ')
    for char in omit_chars:
        if char == words[-1]:
            char_in = words
            for i in range(len(char_in[:-1])):
                char_in[i] = char_in[i][1:] + char_in[i][0] + 'ay'
                final_one = ' '.join(char_in)
            print(final_one)
        elif char != words[-1]:
            for i in range(len(words)):
                words[i] = words[i][1:] + words[i][0] + 'ay'
                final_two = ' '.join(words)
            print(final_two)
        # elif char == words[-1]:
        #     print(words)


pig_it("This is a test sentence !")