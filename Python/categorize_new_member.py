# mine
def open_or_senior(data):
    result = []
    for index, (age, handicap) in enumerate(data):
        if age > 54 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result

# pythonic
def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
