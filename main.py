from turtle import home
import colorama
from colorama import Fore, init
from readscreen import *
import pyautogui as pg

init(convert=True)


words = []
with open('newwords.txt', 'r') as f:
    for line in f:
        words.append(line.strip('\n').lower())

words.sort(key=len)

def menu():
    print('Welcome to my bombparty tool!')
    print('=====================================')
    print('1 - Word by prompt')
    print('2 - Words by length')
    print('3 - Auto Bot')
    print('4 - Quit')
    print('=====================================')
    while True:
        x = input('> ').strip()
        try:
            x = int(x)
            if x in [1, 2, 3, 4]:
                return x
            else:
                print(Fore.RED + 'That is not a valid input.' + Fore.WHITE)
                continue
        except ValueError:
            print(Fore.RED + 'That is not a valid input.' + Fore.WHITE)
            continue



def main():
    option = menu()
    if option == 1: # Words by Prompt
        while True:
            op1 = input('Would you like Longest or Shortest words? (1/2) ')
            try:
                op1 = int(op1)
                if op1 in [1, 2]:
                    break
                else:
                    print(Fore.RED + 'That is not a valid input.' + Fore.WHITE)
                    continue
            except ValueError:
                print(Fore.RED + 'That is not a valid input.' + Fore.WHITE)
                continue
        while True:
            amount = input('How many words would you like per prompt? ')
            try:
                amount = int(amount)
                break
            except ValueError:
                print(Fore.RED + 'That is not a valid input.' + Fore.WHITE)
                continue
        
        if op1 == 1:
            words.sort(key=len, reverse=True)
        else:
            words.sort(key=len)

        while True:
            prompt = input('Enter prompt: ').strip().lower()
            if prompt == 'stop':
                break
            w = []
            for word in words:
                if prompt in word:
                    w.append(word)
            if len(w) < amount:
                for word in w:
                    print(Fore.CYAN + word + Fore.WHITE)
            else:
                for i in range(amount):
                    print(Fore.CYAN + w[i] + Fore.WHITE)
            

    elif option == 2: # Words by Length
        while True:
            op2 = input('How long would you like your words? ')
            try:
                op2 = int(op2)
                break
            except ValueError:
                print(Fore.RED + 'That is not a valid input.' + Fore.WHITE)
                continue
        while True:
            amount = input('How many words would you like per prompt? ')
            try:
                amount = int(amount)
                break
            except ValueError:
                print(Fore.RED + 'That is not a valid input.' + Fore.WHITE)
                continue
        words.sort(key=len)
        w = []
        for word in words:
            if len(word) >= op2:
                w.append(word)
            if len(w) == amount:
                break
        for wod in w:
            print(Fore.CYAN + wod + Fore.WHITE)
    
    elif option == 3:
        print(Fore.GREEN + 'Exit the program with Ctrl+C to quit.' + Fore.WHITE)
        used = []
        words.sort(key=len, reverse=True)
        while True:
            time.sleep(2)
            prompt = readPrompt().lower().strip()
            for word in words:
                if (prompt in word) and not(word in used):
                    w = word
                    break
            used.append(w)
            pg.typewrite(w)
            pg.press('enter') 
            print(prompt + ': ' + w)



    elif option == 4:
        print('Okay, goodbye!')
        exit()


while True:
    main()
