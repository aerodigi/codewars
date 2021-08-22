def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(False)
                return False 
        else:
            print(True)
            return True
    else:
        print(False)
        return False

is_prime(-41)