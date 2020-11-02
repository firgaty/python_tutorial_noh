from random import choice

def get_word_list(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    l = [l.rstrip() for l in lines]
    return l

file_name = 'liste_francais.txt'

words = get_word_list(file_name)

def random_word(words):
    return choice(words)

def converter(words):
    import string
    lc = list(string.ascii_lowercase[:26])
    print(lc)

    f = open("liste.txt", 'w')
    for w in words:
        for e in w:
            if e not in lc:
                print(e, "not in lc.")
                break
        else:
            f.write(w.upper())
            f.write("\n")      
    f.close()


"""

"""