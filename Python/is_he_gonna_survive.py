# mine
def hero(bullets, dragons):
    return True if bullets/2 >= dragons else False

# pythonic
def hero(bullets, dragons):
    return bullets >= dragons * 2
