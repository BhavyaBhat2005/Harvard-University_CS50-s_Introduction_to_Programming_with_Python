#ask user their name
name = input("What's your name? ").strip().title()

#split user's name into first name and last name
first, middle, last = name.split(" ")

#print user's name
print(f"hello, {first} {last}")