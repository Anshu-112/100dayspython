import random
logo= """
 / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|     
"""
print(logo)
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5 

turn=0

def check_answer(user_ans,actual_ans,turns):
    if user_ans==actual_ans:
        print(f"You got it! the answer was {user_ans}")
    elif user_ans>actual_ans:
        print("Too high\n Guess again")
        return turns-1
    else:
        print("Too low \n Guess again")  
        return turns-1  

def difficulty():
    level=input("Choose a difficulty: type 'easy' or 'hard' : ")
    if level=='easy':
        return EASY_LEVEL_TURNS  
    else:
        return HARD_LEVEL_TURNS
def game():    
    print("Welcome to the number Guessing Game!")
    number_to_guess=random.randrange(100)
    print("I am thinking of a number between 1 and 100.")

    turns=difficulty()


    guess=0
    while guess!=number_to_guess:
        print(f"you have {turns} attempts remaining to guess the number.")
      
        guess=int(input("Guess a Number: "))
        turns=check_answer(guess,number_to_guess,turns)
        if turns==0:
            print("YOU've run out of guess.you loss!")
            return 

game()
