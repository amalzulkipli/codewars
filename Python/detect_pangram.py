# my solution
def is_pangram(st):
    lowercased = st.lower() 
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in lowercased:
            return False
    return True
        