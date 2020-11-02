def read_data(file_name):
    file = open(file_name, "r")
    data = []
    for line in file:
        data.append([e.strip() for e in line.split(";")]) # ["Anatomy","1"," @Genre"]
    file.close()
    return data

def format_data(data, init=False):
    CAT = "_"
    formated_data = {CAT : {}}
    
    for d in data:
        l = len(d)
        if l < 2 or l > 3:
            continue
        cat = d[0]
        if cat not in formated_data:
            formated_data[cat] = {}
        key = d[1]
        val = 1
        if l > 2:
            key = d[2]
            val = int(d[1])
        if(init):
            val = 1
        
        formated_data[cat][key] = val
    
    return formated_data

def write_data(file_name, data):
    file = open(file_name, "w+")
    for cat in data:
        for e in data[cat]:
            file.write("{}; {}; {}\n".format(cat, data[cat][e], e))