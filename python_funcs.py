def friend(x):
    '''takes a list of strings and returns strips the list of anything that isn't exactly 4 chars'''
    return [_ for _ in x if len(_) == 4]
