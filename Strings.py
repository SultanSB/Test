# Ask the user for his name
name = input("What is your name ")




# -------------------------------------
# Say hello to the user using his name 

print ("hello,",name) 
print ("=======")

# ------------------------------------

print ("Hello, "+name)
print ("=======")

# -------------------------------------

print ("hello, ", end= "")
print (name)
print ("=======")


# --------------------------------------
# A new way of printing hello name (whatever the user name)

print (f"hello, {name}")
print ("=======")



# ---------------------------------------------
# Remove whitespace from str, only from beggining and from end
# name = name.strip()

# Capitalize user's name (Whether it is first name or last name)
# name = name.title()

# we could use both functions in one line from left to right
name = name.strip().title()


print("Hello,",name)
print ("============")

# --------------------------------------------

# Split function.
name3 = input("Sorry, i will ask you again. What is your full name ")
firstName, middleName, lastName = name3.split(" ")

print ("Your first name is " ,firstName, ". Your middle name ", middleName, ". Your last name", lastName, sep = "")