def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"): #defining hello as a function
    print("hello,", to)

main()
