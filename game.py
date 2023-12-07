import random


random_easy = random.randrange(1, 10)
random_normal = random.randrange(1, 100)
random_hard = random.randrange(1, 1000)
random_impossible = random.randrange(1, 100000000000000000000)


def easy(num):
    """
    This is the easy game mode
    The guessed number, num, is turned into a float.
    Then, the number is checked if it is not equal to the random number.
    If it isn't equal, it checks if it is greater or less than.
        If higher than guessed number, it returns higher.
        If lower than guessed number, it returns lower.
    If it's a negative number, it raises a value error.
    If it's not a string, it raises a type error.
    Otherwise, it returns true which means you win.
    :param num: the guessed number
    :return:
    """
    float_num = float(num)
    try:
        if float_num != random_easy:

            if 0 >= float_num:
                raise TypeError

            elif 0 < float_num < random_easy:
                return f'higher'

            elif float_num > random_easy:
                return f'lower'

        elif float_num == random_easy:
            return True

    except isinstance(num, str):
        raise ValueError


def normal(num):
    """
    This is normal mode.
    The guessed number, num, is turned into a float.
    Then, the number is checked if it is not equal to the random number.
    If it isn't equal, it checks if it is greater or less than.
        If higher than guessed number, it returns higher.
        If lower than guessed number, it returns lower.
    If it's a negative number, it raises a value error.
    If it's not a string, it raises a type error.
    Otherwise, it returns true which means you win.
    :param num: the guessed number
    :return:
    """
    float_num = float(num)
    try:
        if float_num != random_normal:

            if 0 >= float_num:
                raise TypeError

            if 0 < float_num < random_normal:
                return f'higher'

            elif float_num > random_normal:
                return f'lower'
            
        elif float_num == random_normal:
            return True

    except isinstance(num, str):
        raise ValueError


def hard(num):
    """
    This is hard mode.
    The guessed number, num, is turned into a float.
    Then, the number is checked if it is not equal to the random number.
    If it isn't equal, it checks if it is greater or less than.
        If higher than guessed number, it returns higher.
        If lower than guessed number, it returns lower.
    If it's a negative number, it raises a value error.
    If it's not a string, it raises a type error.
    Otherwise, it returns true which means you win.
    :param num: the guessed number
    :return:
    """
    float_num = float(num)
    try:

        if float_num != random_hard:

            if 0 >= float_num:
                raise TypeError

            if 0 < float_num < random_hard:
                return f'higher'

            elif float_num > random_hard:
                return f'lower'
            
        elif float_num == random_hard:
            return True

    except isinstance(float_num, str):
        raise ValueError


def impossible(num):
    """
    This is impossible mode
    The guessed number, num, is turned into a float.
    Then, the number is checked if it is not equal to the random number.
    If it isn't equal, it checks if it is greater or less than.
        If higher than guessed number, it returns higher.
        If lower than guessed number, it returns lower.
    If it's a negative number, it raises a value error.
    If it's not a string, it raises a type error.
    Otherwise, it returns true which means you win.
    :param num: the guessed number
    :return:
    """
    float_num = float(num)
    try:

        if float_num != random_impossible:

            if 0 >= float_num:
                raise TypeError

            if 0 < float_num < random_impossible:
                return f'higher'

            elif float_num > random_impossible:
                return f'lower'

        elif float_num == random_impossible:
            return True

    except isinstance(float_num, str):
        raise ValueError
