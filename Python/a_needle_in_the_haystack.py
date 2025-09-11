# mine
def find_needle(haystack):
    for i, j in enumerate(haystack):
        if j == "needle":
            return f'found the needle at position {i}'

# pythonic
def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'
