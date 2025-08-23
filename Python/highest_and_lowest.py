# my solution
def high_and_low(numbers):
    nums = list(map(int, numbers.split()))
    high = max(nums)
    low = min(nums)
    return f"{high} {low}"

# pythonic
def high_and_low(numbers):
  numbers = [int(c) for c in numbers.split(' ')]
  return f"{max(numbers)} {min(numbers)}"
