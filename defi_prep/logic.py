from random import choices, choice
import re

NUM = [str(a) for a in range(10)]

def is_select(cat):
    return cat[0] == '#'

def is_sub(cat):
    return cat[0] == '@'
    
def sub_select(data, cat, ret_list=[], mode="weighted", ponderate=True, exclude=[]):
    print("SUB-SELECT {}".format(cat))
    for e in sorted(data[cat].keys()):
        ret_list.append(select(data, e[(2 if e[1] == '@' else 1):], [], mode, ponderate, exclude))
    return ret_list

def select(data, cat, ret_list=[], mode="weighted", ponderate=True, exclude=[]):
    """
    mode = ["uniform", "weighted"]
    """
    
    print("SELECT {}".format(cat))
    
    if is_select(cat):
        return sub_select(data, cat, ret_list, mode, ponderate, exclude)
    
    c = None
    population = [key for key in data[cat] if key not in exclude]
    
    if mode == "uniform":
        c = choice(population)
    elif mode == "weighted":
        weights = [1 / data[cat][p] for p in data[cat]]
        print(population)
        print(weights)
        c = choices(
            population=population, 
            weights=weights,
            k=1
        )[0]
    if ponderate:
        data[cat][c] += 1
    if c[0] == '@':
        ret_list.append(c[(2 if c[1] == '#' else 1):])
        return select(data, c[1:], ret_list, mode, ponderate)
    ret_list.append(c)
    return ret_list

def user_choice(data, cat="_", ponderate=True):
    keys = list(data[cat].keys())
    l = len(keys)
    print("1-{} -> Selection | 'Entrer' -> Selection aléatoire:".format(l))

    for i in range(l):
        k = keys[i]
        print("{}: {}".format(i + 1, re.sub(r'@|#|[0-9]', '', k)))
    
    while True:
        c = input().strip()
        if c.isdigit():
            c = int(c)
            if c > 0 and c <= l:
                break
        if c == "":
            return select(data, cat)
            
    cat_ = keys[c - 1]
    
    if is_select(cat):
        cat_ = cat_[1:]
    if is_sub(cat_):
        cat_ = cat_[1:]
    elif cat != '_':
        return cat_
    
    return user_choice(data, cat_)
    