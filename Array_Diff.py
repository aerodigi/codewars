# def array_diff(a, b):
#     c = []
#     for x in a:
#         c.append(x)
#     for y in b:
#         c.append(y)
#         for z in c:
#             if z == y:
#                 c.remove(y)
#         print(c)
# #             elif a == [] and z == y:
# #                 c.remove(y)
# #                 return c
# #                 print("a was", a, "b was", b, "expected", c)
        
# array_diff([1,2],[1])
# array_diff([1,2,2],[1])
# array_diff([1,2,2],[2])
# array_diff([1,2,2],[])
# array_diff([],[1,2])



def array_diff_also(a, b):
    c = []
    for x in a:
        c.append(x)
    for y in b:
        c.append(y)
        while y in c:
                c.remove(y)
    print(c)




array_diff_also([1,2,2],[])