def digitize(n):

    if n == 0:
        return [0]
    
    s = str(abs(n))
    
    reversed_digits = [int(digit) for digit in s[::-1]]
    
    return reversed_digits
