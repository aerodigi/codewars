# def solution():
#     mylist = []
#     sum = 0
#     total = 0

#     while sum < 10:
#         mylist.append(total)
#         sum = sum + 1
#         total = sum + (mylist[-1])
#         print(mylist)
#         print(total)

# solution()


def trial_division(n):
    a = []
    f = 2
    while n > 1:
        if n % f == 0:
            a.append(f)
            n /= f
        else:
            f += 1
    print(a)

trial_division(5000000000000)