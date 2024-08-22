import random

range_number=input("enter the range:")

if range_number.isdigit():
    range_number=int(range_number)

    if range_number<=0:
        print('Enter number larger thn 0 next time')
        quit()
else:
    print('Enter type a number next time')
    quit()

rndom_num=random.randint(0,range_number)

guesses=0
while True:
    user_guess=input('Enter the guess number')
    guesses+=1
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print('Enter type a number next time')
        continue
        

    if user_guess==rndom_num:
        print('You got it')
        break
    elif user_guess>rndom_num:
        print('you were above the number')
    else:
        print('you were below the number')

print('you goy it in',guesses,"guesses")


