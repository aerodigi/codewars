def domain_name(url):
    domain_name_list = url.split('.')
    print(type(domain_name_list))

    for domain in domain_name_list:
        if domain 


    # joining_list = 
    # bs_list = domain_name_list.split('//')
    # print(bs_list)
    # print(domain_name_list)
    # if len(domain_name_list) >= 4:
    #     domain_name_list.remove(domain_name_list[-2])
    # else:
    #     domain_name_list.remove(domain_name_list[0])
    #     domain_name_list.remove(domain_name_list[-1])
    # my_domain_name = ' '.join(domain_name_list)
    # print(my_domain_name)


domain_name("http://google.com")