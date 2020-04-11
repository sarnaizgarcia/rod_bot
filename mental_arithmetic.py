from random import randint


def generate_numbers():
    first_number, second_number = randint(0, 50), randint(0, 50)

    first_list = create_digits_list(first_number)
    second_list = create_digits_list(second_number)

    # función que obitene los números aleatorios
    # función que crea una lista con los dígitos de un número y los iguala en longitud
    # función que
    pass


def create_digits_list(number):
    """ Creates a list with the digits of a number

    Parameters
    ----------
    number: num
        An integer number

    Returns
    -------
    list
        A list of the digits in number parameter
    """
    unordered_digits_list = list()
    while number > 0:
        digit = number % 10
        number = int(number / 10)
        unordered_digits_list.append(digit)
        digits_list = unordered_digits_list[::-1]
    return digits_list


def length_difference(list_a, list_b):
    """ Compares the length of two lists and makes them the same length
    Sees wich is shorter and makes it as long as the other

    Parameters
    ----------
    list_a: list
        First list to compare
    list_b: list
        Second list to compare

    Returns
    -------
    list
        The originally shorter list completed to the length of the other

    """
    difference = len(list_a) - len(list_b)
    if difference == 0:
        return None
    if difference < 0:
        difference = difference * (-1)
        new_list = _extend_list(difference, list_a)
        return new_list
    if difference > 0:
        new_list = _extend_list(difference, list_b)
        return new_list


def _extend_list(positions, list_to_extend):
    """ Extends the length of a list with zeros at the beginning

    Parameters
    ----------
    positions: int
        The positions to be fullfilled

    list_to_extend: list
        A list that will increase its length

    Returns
    -------
    list
        A list with as much zeros at the begining as indicated in positions
    """
    for _ in range(positions):
        list_to_extend.insert(0, 0)
    return list_to_extend


a = [6, 2, 8, 3]
b = [3, 4, 5, 6, 8, 2, 3, 5, 6]
c = [3, 4, 8, 4, 7, 5]

example = create_digits_list(4930585)
print(example)

example_len = length_difference(a, b)
print(example_len)
