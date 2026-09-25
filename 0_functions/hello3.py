#enter name from user

name = input("What's your name? ")

#remove whitespace from str
name = name.strip()

#Capitalize user's name
name = name.title()

#print
print(f"hello, {name}")