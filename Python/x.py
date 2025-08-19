# my solution
def sum_array(arr):
    if arr == None or len(arr) < 2:
        return 0
    arr.remove(max(arr))
    arr.remove(min(arr))
    return sum(arr)

# better pythonic
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)