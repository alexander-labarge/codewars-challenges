# This function determines if the passed value as num is prime.
# This is my solution to https://www.codewars.com/kata/5262119038c0985a5b00029f

def is_prime(num):

    import math

    if num > 1 and int(math.sqrt(num)) ** 2 == num:
        return False
    else:
        if num > 1 and num % num == 0:
            divs = [i for i in range(2,int(math.sqrt(num))+1) if i not in [num]] 
            check_count = len(divs)
            for i in divs:
                if num % i == 0:
                    check_count -= 1
            if check_count < len(divs):
                return False
            else:
                return True
        else:
            return False
