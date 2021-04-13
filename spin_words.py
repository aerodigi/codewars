def spin_words(sentence):
    word_list = sentence.split(" ")
    five_letter_word = []
    other_word_list = []

    for word in word_list:
        if len(word) >= 5:
            five_letter_word = word[::-1]
            other_word_list.append(five_letter_word)
        else:
            other_word_list.append(word)
    
    seperator = ' '
    final_str = seperator.join(other_word_list)
    print(final_str)
    return final_str

spin_words("Hey fellow warriors")


    # Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (like the name of this kata).

    # Strings passed in will consist of only letters and spaces.
    # Spaces will be included only when more than one word is present.



    # take a string, convert into list
