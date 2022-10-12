# function to check if the two necklaces match by moving the first char to the end


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
        
    

k_ary(3, 4)
