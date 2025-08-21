# my solution -- which is wrong miserably, forcing quadratic equation on sum of cubes
import math

def find_nb(m):
    m = (m ** 0.5) * 2
    
    a = 1 
    b = 1 
    c = -m
    
    d = 1 - (4 * 1 * c) 
    
    ans2 = (-b + math.sqrt(d))/(2 * a)
    
    return ans2 if ans2.is_integer() else -1

# better pythonic
import math

def find_nb(m):
    n = int(math.isqrt(2 * math.isqrt(m)))  
    
    while (n * (n + 1) // 2) ** 2 < m:
        n += 1
        
    return n if (n * (n + 1) // 2) ** 2 == m else -1

# and this -- other solution, humbled me down...
def find_nb(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n**3
        if volume == m:
            return n
        n += 1
    return -1

