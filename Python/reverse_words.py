# mine
def reverse_words(text):
    result = []
    for words in text.split(" "):
        result.append(words[::-1])
    return " ".join(result)

# pythonic
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))
