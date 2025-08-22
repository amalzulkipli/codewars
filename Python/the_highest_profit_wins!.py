#my solution
def min_max(lst):
    x = max(lst)
    y = min(lst)
    return [y,x]

#pythonic
def min_max(lst):
  return [min(lst), max(lst)]
