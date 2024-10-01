# Thayer Yang
# 02 OCT 2024
# If Else

from random import randint

# Task 1

age = 18

if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote?')
else:
    print('Sorry, you are too young to vote.')
    print('Please register as soon as you turn 18!')

# Task 2

color = ['green', 'red', 'yellow']

alien = color[randint(0, (len(color)-1))]

if alien == 'green':
    print(f'You got a {alien} alien for 5 points!')
else:
    print(f'You got a {alien} alien for 10 points!')


# Task 3

first_name = input('Enter your first name:\n')

if len(first_name) <=5:
    print(f'Your name is too short {first_name}..')
else:
    print(f'You got a long name {first_name}.')

# Task 4
    
vowels = {'a','e','i','o','u'}
letter = input('Enter a letter from the alphabet: \n')
if letter.lower()[0:1] in vowels:
    print('You printed a vowel, the vowel '+letter.lower()+'.')
else:
    print('You printed the consonant '+letter.lower()+'.')

# Task 5
    
print('Enter two integers:')
int1 = int(input())
int2 = int(input())

if (int1%int2) == 0:
    print(f'The number {int1} is divisible by {int2}.')
else:
    print(f'The number {int1} it not divisible by {int2}.')