
# def array_diff(a,b):
#     for x in a:
#         print("a was", a)
#         for y in b:
#             print(", b was", b)
#             if y in a:
#                 a.pop(y)
#                 print("expected:", a)


# array_diff([1,2],[1])


def array_diff(list1,list2):
    list3 = []
    for x in list1:
        list3.append(x)
    # print(list3)
    for y in list2:
        list3.append(y)
        for z in list3:
            if z == y:
                list3.remove(y)
        print(list3)
    # print(list3)
    # for z in list3:
    #     if z == list2:
    #         list3.remove(z)
    #         print(list3)

array_diff([1,2],[1])