nonogram_row = [0,1,1,1,1,1,0,1,1,1,1]


def nonogram_solver(nonogram):
    return_list = []
    number_tracker = 0
    for x in nonogram:
        if x:
            number_tracker += 1
        else:
            if number_tracker:
                return_list.append(number_tracker)
                number_tracker = 0
    if number_tracker:
        return_list.append(number_tracker)
    return return_list

print(nonogram_solver(nonogram_row))