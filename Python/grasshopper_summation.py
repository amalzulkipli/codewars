# mine
def summation(num):
    result = 0
    for i in range(1,num+1):
        result += i
    return result
    
# pythonic
def summation(num):
    return sum(range(1,num+1))
