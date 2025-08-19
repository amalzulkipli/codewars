# my solution
def array_diff(a, b):
    result = []
    for x in a:
        if x not in b:
            result.append(x)
    return result

# better pythonic solution
def array_diff(a, b):
    return [x for x in a if x not in b]