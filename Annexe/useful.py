def to_number(a):
    if a.is_digit():
        return int(a)
    elif a[0] == '-' and a[::1].is_digit():
        return - int(a[::1])
    return None