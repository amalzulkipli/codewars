# my sol
def stray(arr):
    for i in arr:
        if arr.count(i)==1:
            return i

# pythonic
def stray(arr):
    return min(arr, key=arr.count)
