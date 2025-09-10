# mine
def alphabet_position(text):
    result = []
    text = [char for char in text if char.isalpha()]
    for i in text:
        result.append(ord(i.lower()) - 96)
    result = " ".join(str(n) for n in result)
    return result

# pythonic
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
