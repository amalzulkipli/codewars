# my sol
def combine(*arrays):
    result = []
    max_len = max(len(arr) for arr in arrays)  
    
    for i in range(max_len):  
        for arr in arrays:          
            if i < len(arr):        
                result.append(arr[i])
    return result

# pythonic
def combine(*args):
  out = list()
  for i in range(len(max(args, key=len))):
    for arr in args:
      if i < len(arr): out.append(arr[i])
  return out
