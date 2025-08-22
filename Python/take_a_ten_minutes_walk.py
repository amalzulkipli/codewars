# my solution
def is_valid_walk(walk):    
    condition_1 = len(walk) == 10
    
    mapping = { "n": (0, 1), "s": (0, -1), "e": (1, 0), "w": (-1, 0) }
    x, y = 0, 0
    
    for move in walk:
        dx, dy = mapping[move]  
        x += dx
        y += dy     
    
    
    condition_2 = (x, y) == (0, 0) 
    
    if condition_1 == True and condition_2 == True:
        return True
    else:
        return False

