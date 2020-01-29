a = 3
a**2


a==3

a+1 >= 2 and a**2 != 5

a**2 >= 9 and not a>3

a+2 == 5 or a-1 != 3

# Prediction True

a**2 >= 9 and not a>3

# Prediction True

a+2 == 5 or a-1 != 3



def age_limit_output(age) :

    AGE_LIMIT = 13
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' minimum age is ', AGE_LIMIT)

age_limit_output(10)
age_limit_output(16)

def report_grade(percent) :

    GRADE_CUTOFF = 80
    if percent >= GRADE_CUTOFF:
        print('A grade of ', percent, ' indicates mastery.' )
        print(' Keep up the good work!')
    else:
        print('A grade of ', percent, ' doesnt indicate mastery.' )
        print(' Youre garbage. Absolute trash.')

report_grade(70)
report_grade(80)

def letter_in_word(guess, word) :
    if guess in word:
        print(guess, ' is in word. Wow')
    else:
        print('you are garbage')

letter_in_word('t', 'secret hangman phrase')



def hint(color, secret):
    if color in secret:
        print (color, ' is there')
    else
        print (color, ' isnt in the code. You absolute plebian' )


 secret = ['red','red','yellow','yellow','black']
 hint('red', secret)