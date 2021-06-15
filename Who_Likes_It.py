def likes(names):
    number_of_names = len(names)
    print(names)
    if number_of_names < 1:
        print ("no one likes this")
    elif number_of_names == 1: 
        print(names[0], "likes this")
    elif number_of_names < 3:
        print(names[0],'and',names[1],'like this')
    elif number_of_names < 4:
        print(names[0],',',names[1],'and',names[2],'like this')
    elif number_of_names > 3:
        print(names[0],',',names[1],'and',number_of_names - 2,"others like this")

    # if people == []:
    #     print("no one likes this")
    #     print(people,"likes this")
    # elif people[0]
    # pass

# list_of_names = ["Martin", "Stuart", "Samuel", "Peter", "James"]
likes([])
likes(['Peter'])
likes(['Jacob', 'Alex'])
likes(['Max', 'John', 'Mark'])
likes(['Alex', 'Jacob', 'Mark', 'Max'])
       