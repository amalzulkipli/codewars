# my solution
def quarter_of(month):
    month_dict = {1: [1,2,3], 2: [4,5,6], 3: [7,8,9], 4: [10,11,12]}
    for k, v in month_dict.items():
        if month in v:
            return k
    return None 

# better pythonic solution
def quarter_of(month):
    return (month + 2) // 3