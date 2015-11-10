import person

again = True

while again:
    name = raw_input("Enter your name: ")
    age = input("Now, enter your age: ")
    you = person.person(name, age)
    name = raw_input("Enter your friend's name: ")
    prompt = "Now, enter " + name + "'s age"
    age = input(prompt)
    friend = person.person(name, age)

    if you.age > friend.age:
        print you.name + ", you are older than " + friend.name
    elif friend.age > you.age:
        print you.name + ", you are younger than " + friend.name
    else:
        print you.name + ", you and your friend, " + friend.name + ", are of equal age!"

    repeat = raw_input("Do you want to do this again? (Y/N): ").upper()
    if repeat == "N":
        again = False
        print "Okay, bye"
