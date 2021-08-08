def flatten_function(list_):
    """
    This function flattens the entered layered list, that is, makes it a single layered list.
    :param: list_
    :return: empty_list
    """
    # An empty list to save the changes that have been made
    empty_list = []

    for index in list_:
        if type(index) is list:
            for i in index:
                empty_list.append(i)
        else:
            empty_list.append(index)

    for i in empty_list:
        if type(i) is list:
            return flatten_function(empty_list)
    return empty_list


def reverse_function(list_):
    """
    This function reverses the elements in the given list. If the elements inside the list also contain the list,
    it also reverses their elements.
    :param: list_
    :return: empty_list
    """
    empty_list = []
    list_.reverse()

    for index in list_:
        empty_list.append(index)

    for i in empty_list:
        if type(i) is list:
            i = i.reverse()
    return empty_list


if __name__ == '__main__':
    print(flatten_function([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]))
    print(reverse_function([[1, 2], [3, 4], [5, 6, 7]]))
