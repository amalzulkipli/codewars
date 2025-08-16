# my solution
def double_char(s):
    new = ""
    for letter in s:
        new += letter*2
    return new

# better pythonic way
def double_char(s):
    return ''.join(c * 2 for c in s)