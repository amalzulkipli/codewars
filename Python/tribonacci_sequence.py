# my solution
def tribonacci(signature, n):
    if n == 0:
        return []
    if n < len(signature):
        return signature[:n]

    result = signature[:]  
    while len(result) < n:
        result.append(sum(result[-3:])) 
    return result

# better pythonic
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res