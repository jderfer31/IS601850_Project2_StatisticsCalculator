def check(data):
    try:
        data[0]
        return data
    except IndexError:
        return None
