# scope

# global scope
name = "Bro"



# local scope
def display_name():
    name = "Code"
    print(name)

display_name()
print(name)