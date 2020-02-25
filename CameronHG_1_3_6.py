import random

#a = (6, 7, 9)

some_values = ('a', 'b', 3)

#print(some_values[0:2])

a = 10
tup = (9, a, 11)

print(tup[1] == 10)

print(tup[1])

values = [1, 2, 3]
print(values[1:])

values2 = ['a','b','c']

values2[2] = '3'

print(values[2] == 3)

values += [4, 5]
print(values)

values.append([6,7])
print(values)



a = 6
a *= 3
print(a)

def roll_two_dice():
    dieOne = random.randint(1, 6)
    dieTwo = random.randint(1, 6)
    dieSum = dieOne + dieTwo

    print(dieSum)
roll_two_dice()