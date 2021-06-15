def pig_it(text):
    words = text.split(' ')
    for i in range(len(words)):
        words[i] = words[i][1:] + words[i][0] + 'ay'
    print(' '.join(words))
    

pig_it("Quis custodiet ipsos custodes ?")
    
        # i.split(list_of_words)
        # print(i)
    # if text == "Pig latin is cool":
    #     return(text[1:3] + text[0] + "ay " + text[5:9] + text[4] + "ay " + text[11] + text[10] + "ay " + text[14:] + text[13] + "ay")
    # elif text == "This is my string":
    #     return(text[1:4] + text[0] + "ay " + text[6] + text[5] + "ay " + text[9] + text[8] + "ay " + text[12:] + text[11] + "ay")

    
    
# .strip space[-1]
# .split space[-1]



def remove_and_add(text):
    words = text.split(' ')
    print(words)
    if words[-1] != "!" or "?":
        for i in range (len(words)):
            print(i)
            words[i] = words[i][1:] + words[i][0] + 'ay'
        print(' '.join(words))
    # else:
    #     lw = []
    #     lw.append(words[-1])
    #     words.remove(words[-1])
    #     for i in range (len(words)):
    #         words[i] = words[i][1:] + words[i][0] + 'ay'
    #     punct = ' '.join(lw)
    #     words.append(punct)
    #     print(' '.join(words))



remove_and_add("Jennifer Lopez is from the block !")
remove_and_add("Chaz and Dave were here")
remove_and_add("Ashley is the very best !")
remove_and_add("Who has my Dog ?")
remove_and_add("yes sir")
remove_and_add("What on earth was that?!")