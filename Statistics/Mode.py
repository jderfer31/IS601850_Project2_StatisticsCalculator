def mode(data):
    dict = {}
    for val in data:
        if dict.get(val) is None:
            dict[val] = 1
        else:
            dict[val] = dict[val]+1
    max_count = max(dict.values())
    mode = [k for k, v in dict.items() if v == max_count]
    return mode