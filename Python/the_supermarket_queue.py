# mine (AI)
def queue_time(customers, n):
    if not customers:
        return 0
    
    tills = [0] * n
    for customer in customers:
        shortest_till = tills.index(min(tills))
        tills[shortest_till] += customer
    return max(tills)
