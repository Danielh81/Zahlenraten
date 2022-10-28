import random

min = 1
max = 100
number = random.randint(min, max)
name = input("Wie lautet ihr Name: ")

while len(name) == 0:
    name = input("Bitte geben Sie erneut Ihren Namen ein: ")
   
print(f'Hallo, {name}! Ich denke an eine Zahl zwischen {min} und {max}. Welche Zahl ist es?.')

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
        
        if guess < min:
            print(f'Deine Zahl ist zu klein! ({min}-{max})')   
            continue     
        if guess > max:  
            print(f'Deine Zahl ist zu groß! ({min}-{max})')  
            continue

        difference = abs(number-guess)
        
        if difference <= 5 and guess != number: 
            print('heiß')        
        elif difference >= 6 and difference <= 10:
            print ('schon wärmer')           
        elif difference >= 11:
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

    while True:
        nochmal = input('Noch einmal? (j/n)')
        if nochmal == 'j':
            print("Here we go again!")
            number = random.randint(min, max)
            count = 0      
            break   
        elif nochmal == 'n':
            running = False
            print("Schade, vielleicht an anderes mal.")
            break         
        else:
            print('Bitte nur mit j/n antworten')    
