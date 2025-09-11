# mine
def tower_builder(n_floors):
    counter_1 = 1
    counter_2 = n_floors-1
    result = []
    for i in range(1,n_floors+1):
        tree = " "*counter_2 + "*"*counter_1 + " "*counter_2
        result.append(tree)
        counter_1+=2
        counter_2-=1
    return result

# pythonic
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
