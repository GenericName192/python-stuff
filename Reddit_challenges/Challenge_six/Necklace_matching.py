# function to check if the two necklaces match by moving the first char to the end
import math
import itertools

def necklace_checker(necklace_one: str, necklace_two: str):
    """
    :arg necklace_one - This is the first necklace, it is maniuplated through the splice of the string to check if it can match the first necklace
    :arg necklace_two - This is the second necklace, used as a base to compare the other to.
    :return - Returns a string to let you know if they match.
    """
    if len(necklace_one) != len(necklace_two):
        return False

    for char in necklace_one:

        if necklace_one != necklace_two:
            necklace_one = necklace_one[1:]
            necklace_one += char

        else:
            return True

    return False

def k_ary(n: int, l: int):
    counted = []
    necklace = [0] * l
    should_exit = False
    # [0,0,0,0,0]
    while not should_exit:
        necklace_string = (necklace)
        found = False
        for char in necklace:
            if str(necklace_string) in counted:
                found = True
            necklace_string = necklace_string[1:]
            necklace_string += [char]
        if not found:
            counted.append(str(necklace)) 
        necklace[-1] += 1
        for i in reversed(range(len(necklace))):
            #[0, 0, 9]
            if necklace[i] > n - 1:
                if i == 0:
                    should_exit = True
                necklace[i - 1] += 1
                necklace[i] = 0
    print(len(counted))       
        
    




# No idea how this works, copied it
def prime_factors(n):
    factors = []
    while n % 2 == 0:
        if 2 not in factors:
            factors.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            if i not in factors:
                factors.append(i)
            n = n // i
    if n > 2 and n not in factors:
        factors.append(n)
    return factors

def phi(a):
    if a <= 1:
        return 1
    # how many numbers less than a don't have any common factors except for 1
    # e.g a = 12
    # all numbers less than 6 = [1,2,3,4,5,6,7,8,9,10,11]
    # 12's prime factors are 2*2*3
    # 2,4,6,8,10 each have a common factor of 2
    # 3,6,9 each have a common factor of 3
    # so 2,3,4,6,8,9,10 all have some factor in common
    # which numbers are left? 1,5,7,11
    # return 4

    # e.g a = 12
    count = 0
    factors_of_a = prime_factors(a) # [2,3]
    for n in range(1,a): # n = 1, 2, 3, 4, 5, 6...
        factors_of_n = prime_factors(n) # [], [2], [3], [2], [5], [2,3] ...
        found_common_factor = False
        for factor_of_n in factors_of_n: # go through all factors of n
            if factor_of_n in factors_of_a: # if there's any factors in common with a, then ignore
                found_common_factor = True
                break

        if not found_common_factor: # if, after going through all factors of n, we haven't found any factors in common then add 1 to count
            count += 1
    return count

def necklace(k, n):
    sum = 0
    for a in range(n + 1):
        for b in range(n + 1):
            if a * b == n:
                sum += phi(a) * (k ** b)

    return (1/n) * sum

print(necklace(13, 12))


