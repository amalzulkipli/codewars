# my sol
def powers_of_two(n):
    counter = 0
    result = []
    while counter < n+1:
        result.append(2**counter)
        counter += 1
    return result

# pythonic
def powers_of_two(n):
    return [2**x for x in range(n+1)]
