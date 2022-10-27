
from curses.ascii import isdigit
import random

min = 1
max = 100
number = random.randint(min, max)
name = input("Wie lautet ihr Name: ")

while len(name) == 0:
    name = input("Bitte geben Sie erneut Ihren Namen ein: ")
   
print(f'Hallo, {name}! Ich denke an eine Zahl zwischen 1 und 100. Welche Zahl ist es?.')

count = 0
running = True

while running:
    while True:
        
        while (True) :
            guess = input()
            if(guess.isnumeric()):
                break
            else:
                print('Das ist keine Zahl')
        
        guess = int(guess)
        x = abs(number-guess)
        if x <= 5: 
            print ('heiß')
        elif x >= 6 and x <= 10:
            print ('schon wärmer')    
        elif x >= 11:
            print ('leider kalt')    

        if guess < number:
            print('Deine Versuch ist zu niedrig. Rate erneut!')
            count += 1
            print(f'Deine Versuche: {count}')
            
        if guess > number:
            print('Dein Versuch ist zu hoch. Rate erneut!')
            count += 1
            print(f'Deine Versuche: {count}')

        if guess == number:
            print(f'Gut gemacht! Du hast die richtige Zahl erraten!')
            count += 1
            print(f'Deine Versuche: {count}')
            break

        if guess < min:
            print(f'Deine Zahl ist zu klein! ({min}-{max})')
        if guess > max:  
            print(f'Deine Zahl ist zu groß! ({min}-{max})')  


    nochmal = input('Noch einmal? (j/n)')
    if nochmal == 'j':
        print("Here we go again!")
        count = 0
    
    if nochmal == 'n':
        running = False
        print("Schade, vielleicht an anderes mal.")
