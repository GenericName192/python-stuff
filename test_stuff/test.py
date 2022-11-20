def two_sum(numbers, target):
    for x in numbers:
        copy_list = numbers[:]
        copy_list.remove(x)
        checker = target - x
        if checker in copy_list:
            if checker == x:
                indexs_of_x = [ i for i in range(len(numbers)) if numbers[i] == x ]
                if len(indexs_of_x) > 2:
                    return indexs_of_x[:2]
                return indexs_of_x
            else:
                return numbers.index(x), numbers.index(target - x)



        
print(two_sum([2,2,3], 4))