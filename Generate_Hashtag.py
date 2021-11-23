def generate_hashtag(s):
    upper = s.title()
    updated_text = "".join(upper.split())
    my_list = []
    if len(updated_text) == 0:
        return False
    elif len(updated_text) > 139:
        return False
    else:
        for x in updated_text:
            my_list += x
        my_list.insert(0, "#")
        updated_list = "".join(my_list)
        stripped_list = updated_list.strip()
        return stripped_list


generate_hashtag("Code wars is nice")
