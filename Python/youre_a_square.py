# my solution
def is_square(n):
    if n < 0:
        return False
    x = n ** 0.5
    return x.is_integer()

# better pythonic solution
def is_square(n):    
    return n >= 0 and (n**0.5) % 1 == 0