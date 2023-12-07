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
    If the guessed number is lower than the random number, it returns higher.
    If the guessed number is higher than the random number, it returns lower.
    Otherwise, it returns true which means you win.
    :param num:
    :return:
    """
    float_num = float(num)
    if float_num != random_easy:
        if float_num < random_easy:
            return f'higher'
        elif float_num > random_easy:
            return f'lower'
    else:
        return True


def normal(num):
    """
    This is normal mode.
    The guessed number, num, is turned into a float.
    Then, the number is checked if it is not equal to the random number.
    If it isn't equal, it checks if it is greater or less than.
    If the guessed number is lower than the random number, it returns higher.
    If the guessed number is higher than the random number, it returns lower.
    Otherwise, it returns true which means you win.
    :param num:
    :return:
    """
    float_num = float(num)
    if float_num != random_normal:
        if float_num < random_normal:
            return f'higher'
        elif float_num > random_normal:
            return f'lower'
    else:
        return True


def hard(num):
    """
    This is hard mode.
    The guessed number, num, is turned into a float.
    Then, the number is checked if it is not equal to the random number.
    If it isn't equal, it checks if it is greater or less than.
    If the guessed number is lower than the random number, it returns higher.
    If the guessed number is higher than the random number, it returns lower.
    Otherwise, it returns true which means you win.
    :param num:
    :return:
    """
    float_num = float(num)
    if float_num != random_hard:
        if float_num < random_hard:
            return f'higher'
        elif float_num > random_hard:
            return f'lower'
    else:
        return True


def impossible(num):
    """
    This is impossible mode
    The guessed number, num, is turned into a float.
    Then, the number is checked if it is not equal to the random number.
    If it isn't equal, it checks if it is greater or less than.
    If the guessed number is lower than the random number, it returns higher.
    If the guessed number is higher than the random number, it returns lower.
    Otherwise, it returns true which means you win.
    :param num:
    :return:
    """
    float_num = float(num)
    if float_num != random_impossible:
        if float_num < random_impossible:
            return f'higher'
        elif float_num > random_impossible:
            return f'lower'
    else:
        return True
