import random

animals = ['cat', 'dog', 'fish']
chosen_word = random.choice(animals)

guess = input('Enter a letter').lower()

for letter in chosen_word:
    if guess == letter:
        print("right")
    else:
        print('wrong')


