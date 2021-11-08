'''
Hangman for numbers
Objective : Identify the number by guessing possible digits to fill in the blanks.
            You get a hint before the final chance.
            You get penalized for guessing the wrong digit or an already used digit, maximum of 2 mistakes can be made.
            There is no entry limit.

Possible hints:
- If only one digit is left to be guessed, hint at whether the digit is odd or even.
- If more than one digit is left to be guessed (with duplicates), hint at the sum of the remaining digits.
Note : Hint can appear only once.
'''

import random
from subprocess import call
from time import sleep,time
import os
import pandas as pd
from datetime import datetime
import string


def clear():
    '''
    clear terminal screen after one game session
    '''
    _ = call('clear' if os.name == 'posix' else 'cls')
def get_index(l, a):
    '''
    return index(es) of a digit present in a list
    '''
    p = l
    r = []
    while (1):
        try:
            i = p.index(a)
            r.append(i)
            p[i] = '$'
        except:
            return r
def get_hint():
    '''
    provide hint based on game status
    '''
    index = get_index(list(subs), "_")
    print(f"Only {len(index)}", "digit(s) left")
    if len(index) == 1:
        number = int(ar[index[0]])
        if number % 2 == 0:
            hint = "It is an even digit."
        else:
            hint = "It is an odd digit."
    else:
        sum_ = 0
        for ind in index:
            sum_ += int(ar[ind])
        hint = f"Sum of missing digits = {sum_}"
    print("!!! Hint : ", hint, " !!!")
def draw_hangman(saved=False):
    chance0="   _______\n   |     +\n   C     +\n~--|--~  +\n   |     +\n   |     +\n _/ \_   +\n==========="
    chance1="   _______\n   |     +\n   C     +\n~--|--~  +\n   |     +\n         +\n         +\n==========="
    chance2="   _______\n   |     +\n   C     +\n         +\n         +\n         +\n         +\n==========="
    chance3="   _______\n   |     +\n         +\n         +\n         +\n         +\n         +\n==========="
    safe   ="          \n          \n   C      \n~--|--~   \n   |      \n   |      \n _/ \_    \n"
    if saved:
        print(safe)
    else:
        if chance==3:
            print(chance3)
        elif chance==2:
            print(chance2)
        elif chance==1:
            print(chance1)
        else:
            print(chance0)
def play():
    '''
    one function call represents one game
    '''
    global subs,ar,new_game,win,list_to_append,chance
    win=False
    chance = 3
    numbers = "0 1 2 3 4 5 6 7 8 9".split()
    p = random.randint(100000, 999999)
    s = str(p)
    subs = ""
    ar = []
    for i in range(len(s)):
        subs += "_"
        ar.append(s[i])

    guessed = []
    hint_left = True
    list_to_append = []
    while (1):
        print("-----------------------------------------------------------------------")
        dt = datetime.now()
        digits_left=len(get_index(list(subs), "_"))
        hint_given=(not hint_left)
        chances_left=chance
        if subs == s:
            sing = ''
            if chance > 1:
                sing = 's'
            draw_hangman(saved=True)
            print(f"CONGRATULATIONS! You have won the game with {chance} chance{sing} to spare!")
            print(f"NUMBER : {s}")
            win=True
            list_to_append.append([user_id, dt, session_id, game_no, chances_left, digits_left, n, hint_given, win])
            new_game = input("New game? (y/n) : ")
            break
        if chance == 0:
            draw_hangman()
            print("Game over! You havent guessed the right number :(")
            print(f"NUMBER : {s}")
            list_to_append.append([user_id, dt, session_id, game_no, chances_left, digits_left, n, hint_given, win])
            new_game = input("New game? (y/n) : ")
            break

        if (chance == 1) & (hint_left):
            get_hint()
            hint_left = False

        # Display
        print("Number to guess : ", " ".join([char for char in subs]))
        print("Chances left : ", chance)
        draw_hangman()
        n = input("Enter a single digit whole number : ")

        # validating entry
        while (n not in numbers):
            n = input("Invalid entry...Enter a single digit whole number : \n")
            if n in numbers:
                break
        # testing presence
        if n in guessed:
            print("You have already used this digit. Try a new one.")
            chance -= 1
        elif n in ar:
            guessed.append(n)
            indices = get_index(ar, n)
            for ind in indices:
                subs = subs[:ind] + n + subs[ind + 1:]
        else:
            print(f"Does not contain the digit {n}.")
            chance -= 1
        list_to_append.append([user_id,dt,session_id,game_no,chances_left,digits_left,n,hint_given,win])



# Play
user_id = input("Enter user name : ")
df=pd.DataFrame(columns=['user','datetime','session_id','game_no','chances_left','digits_left','input','hint_given','win'])
game_no=0
session_id=str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)))
start_time=time()
while(1):
    game_no+=1
    play()
    df=df.append(pd.DataFrame(list_to_append,columns=df.columns),ignore_index=True)
    if new_game!='y':
        df.to_csv(f"Database/{user_id}_{session_id}_{str(datetime.now())}.csv")
        print("Thanks for playing! Your game data is saved")
        print("Session time : ",round(time()-start_time,2)," seconds")
        sleep(3)
        clear()
        break