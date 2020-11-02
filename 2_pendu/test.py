name = "John"
sname = "Doe"

s = f"My name is {sname}, {name} {sname}."
s_ = "My name is {sname}, {name} {sname}.".format(sname = sname, name = name)

print(s)
print(s_)