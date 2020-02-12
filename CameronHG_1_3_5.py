from __future__ import print_function

slogan = "My school is the best"



print(slogan[:13] + "Awesome!")

activity = 'theater'

print(len(activity))
print(activity[0 : len(activity)-1 ])


def greatest_good():
    if "test goo" in "Greatest good for the greatest number!":
        print("It's in, chief")
    else:
        print("Nah")

greatest_good()

def how_eligible(essay):
    char = 0

    if "?" in essay:
        char += 1
    if "!" in essay:
        char += 1
    if "." in essay:
        char += 1
    if "," in essay:
        char += 1

    print(str(char) + " characters in essay")
    if char == 4:
        print("You used all the characters! Congrats on your adequate grammatical ")


how_eligible('This? "Yes." No, not really!')

a = 'one string'
b = 'another'
c = a[:3] + ' and ' + b
print(c[6:10])
