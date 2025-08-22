# my solution
def update_light(current):
    if current == 'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    else:
        return 'green'

# pythonic
def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]
