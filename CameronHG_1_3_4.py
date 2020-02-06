from __future__ import print_function # must be first in file

def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']
    # Check the category and report
    if food in fruits:
        if food in citrus:
            print('orange')
            return 'Citrus, Fruit'
        else:
            print('apple or banana')
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'




# ------------------------------------------------------------------------------------

def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not good
    '''

    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()'
    # Add tests so that all lines of code are visited during test

    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False

food_id_test()
#---------------------------------------------------------------------------------------


def f(n):

    if int(n)==n:


        if n%2 == 0:
            if n%3 == 0:
                print('N is a multiple of 6')

            else:
                print('N is even')

        else:
            print('N is odd')
    else:
        print("N isn't an integer")

f(8)
f(6)

print('---------------------------------------------------------------------------')




import random

def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4 inclusive')
    guess = int(input('Guess: '))
    if guess == secret:
        print('Right on! My number was ', guess, end='!\n')

    else:
        if guess > secret:
            print("Too high, my number was",secret, end='!\n')
        else:
            print("Too low, my number was", secret, end='!\n')
guess_once()


