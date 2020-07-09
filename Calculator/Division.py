def division(a, b):
    try:
        c = float(b) / float(a)
        return c
    except ZeroDivisionError as err:
        raise err


