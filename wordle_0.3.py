from randomword import listWords
from curses.ascii import isalpha, isdigit
import random
import time


word = random.choice(listWords).upper()
counter = 0
running = True
valid = True

while running == True:
    
    if counter == 0:

        print('''
        HOW TO PLAY

        Guess the word in 15 tries
        
        - Each guess must be a valid 5-letter word
        
        - The case of letters will change to show how close your 
        guess was to the word
        
        Example:
        
        Your guess: skate
        S - uppercase is in the word and in the correct spot
        _
        a - lowercase is in the word but in the wrong spot
        _
        _
        ''')

    time.sleep(0.5)

             
    while valid == True:
        
        guess = input('\nYour guess : ')  
              

        if guess.isalpha() == True and len(guess) == len(word):
            guess = guess.upper()
            break
            

        else:
            
            time.sleep(0.075)

            print(f'''
        Invalid word: {guess}
        Guess word should consists of 5 letter
        Guess word allow only letters 
        No spaces, no symbols, no digits and etc
            ''')
            

    for i in range(len(guess)):                          # цикл робит 5 раз, зависит от дилнны слова

        if word[i] == guess[i]:
            time.sleep(0.15)                             # проверяем есть ли на текущей итерации цикла, буква из слова 
            print(f'{guess[i].upper()}  Definitely')     # то есть тут мы проверяем есть ли буква на нужной позиции
            
        elif word.find(guess[i]) != -1:
            time.sleep(0.15)                             # если первое условие не сработало, то здесь проверяем:
            print(f'{guess[i].lower()}  Wrong place')    # есть ли в guess слове вообще буква из word на любой позиции
                                        
        else:
            time.sleep(0.15)
            print('_')
            
    counter += 1
    
    if counter < 15:
        print(f'\n{15 - counter} tries left') 

    if guess == word:
        print(f'\n Congratulations! \n\nYou did it with {counter} tries')
        running = False

    elif counter >= 15:
        print(f'The word was : {word}')
        running = False
    


__version__ = '0.3'



