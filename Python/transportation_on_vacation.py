#my sol
def rental_car_cost(d):
    if d < 3:
        return d*40
    elif d < 7:
        return (d*40)-20
    else:
        return (d*40)-50

def rental_car_cost(d):
  return d * 40 - (d > 2) * 20 - (d > 6) * 30
