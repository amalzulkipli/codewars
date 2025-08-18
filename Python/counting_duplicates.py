# my solution
def duplicate_count(text):
    text = text.lower()
    counter = 0
    for letter in set(text):
        if text.count(letter) > 1:
            counter += 1
    return counter

# better pythonic solution
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])