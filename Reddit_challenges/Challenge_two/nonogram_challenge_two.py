nonogram = """ 0 1 1 1 1 0
1 0 0 1 1 1
1 0 1 1 1 1
1 1 1 1 1 1
0 1 1 1 1 0 """

def nonogram_sorter(nonogram: str):
    sortednonogram = nonogram.replace(" ", "")
    sortednonogram = sortednonogram.split("\n")
    temp_list = []
    return_list = []
    number_tracker = 0
    for lists in sortednonogram:
            
        for chars in lists:

            if chars == "1":
                number_tracker += 1

            else:
                if number_tracker:
                    temp_list.append(number_tracker)
                    number_tracker = 0

        if number_tracker:
            temp_list.append(number_tracker)
            number_tracker = 0 

        return_list.append(temp_list)
        temp_list = []
    return return_list

for x in nonogram_sorter(nonogram):
    print(x)


# def char_checker(string):
#     number_tracker = 0
#     return_list = []
#     length = len(string)
#     index = 0
#     for char in string:
#         if char == "1":
#             number_tracker += 1
#         else:
#             if number_tracker:
#                 return_list.append(number_tracker)
#                 number_tracker = 0
#         index += 1
#         if index == length:
#             if number_tracker:
#                 return_list.append(number_tracker)
#     return return_list

