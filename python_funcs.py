def friend(x):
    '''takes a list of strings and returns strips the list of anything that isn't exactly 4 chars'''
    return [_ for _ in x if len(_) == 4]

def is_triangle(a, b, c):
    '''given a, b, and c returns boolean value based on if the values can form a valid 
    triangle (Triangle Inequality Theorem) a + b > c; a + c > b; b + c > a'''
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
