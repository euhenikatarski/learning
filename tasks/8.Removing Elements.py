def remove_every_other(my_list):
    new_lst = []
    for i, element in enumerate(my_list):
        if i % 2 == 0:
            new_lst.append(element)
    return print(new_lst)

