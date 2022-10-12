from random import randrange


pancake_list = [1, 4, 3, 4, 5, 6]

def flipfront(number):
    reverse_list = pancake_list[:number]
    reverse_list.reverse()
    index = 0
    for num in reverse_list:
        pancake_list[index] = reverse_list[index]
        index += 1

def sort_list():
    sorted_list = pancake_list[:]
    sorted_list.sort()
    return sorted_list

def flip_till_sort():
    sorted_list = sort_list()
    count = 0
    while pancake_list != sorted_list:
        flipfront(randrange(len(pancake_list) + 1))
        print(pancake_list, count)
        count += 1

flip_till_sort()
