# my sol
def human_years_cat_years_dog_years(human_years):

    if human_years == 1:
        cat_years = 15
    elif human_years == 2:
        cat_years = 15+9
    else:
        cat_years = 15+9+(4*(human_years-2))
        
    if human_years == 1:
        dog_years = 15
    elif human_years == 2:
        dog_years = 15+9
    else:
        dog_years = 15+9+(5*(human_years-2))
    
    return [human_years,cat_years,dog_years]

# pythonic
def human_years_cat_years_dog_years(n):
    cat_years = 15 + (9 * (n > 1)) + (4 * (n - 2) * (n > 2))
    dog_years = 15 + (9 * (n > 1)) + (5 * (n - 2) * (n > 2))
    return [n, cat_years, dog_years]
