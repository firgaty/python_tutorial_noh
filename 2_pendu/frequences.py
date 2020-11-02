import string

def get_word_list(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    l = [l.rstrip() for l in lines]
    return l

file_name = 'liste_fr.txt'

words = get_word_list(file_name)
upper = list(string.ascii_uppercase[:26])
occ = dict.fromkeys(upper, 0)

for w in words:
    for l in set(w):
        occ[l] += 1
            
print(occ)
occ = {k: v for k, v in sorted(occ.items(), key=lambda item: item[1], reverse=True)}
s = ""
for e in occ:
    s += str(e) + " "
print(s)