# we are going to make function saying only (hello, the name of the user)

# this is the function
# it is the deafault value if the argument is not provided by the user
def hello(name = "World"):
    print("Hello", name)
# =======================

name = input ("What is your name? ")
hello(name)


# ==========================
# This function returns a name
def yourName (x = "None"):
    return x
# ==========================

myName = yourName("sultan")
print(myName)

