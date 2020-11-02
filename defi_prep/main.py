import IOHandler as ioh
import logic as log
import sys

# Default arguments
data_in = "data"
data_out = "data_bis"
init_ponderation = False
format_data = False

# Gestion des arguments CLI
if len(sys.argv) >= 2:
    bool_val = lambda val: True if int(val) == 1 else False
    for arg in sys.argv[1:]:
        (param, val) = arg.split("=")
        if param == "in":
            data_in = val
        elif param == "out":
            data_out = val
        elif param == "init":
            init_ponderation = bool_val(val)
        elif param == "format":
            format_data = bool_val(val)
    
# Programme
data = ioh.read_data(data_in)
data = ioh.format_data(data, init=init_ponderation)

if format_data:
    ioh.write_data(data_out, data)
    exit(0)

print(data)

# c = log.select(data, "Anatomie")
# print(c)
# print(log.select(data, c, mode="uniform"))

print(log.user_choice(data))

ioh.write_data(data_out, data) 