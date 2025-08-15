def persistence(n):
    count = 0
    while len(str(abs(n))) > 1:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        count += 1
    return count
    