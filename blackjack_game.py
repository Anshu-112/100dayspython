import random


def deal_card():
     cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
     return random.choice(cards)     

def calculate_score(cards):
     if sum(cards) == 21 and len(cards) == 2:
          return 0
     while 11 in cards and sum(cards)>21:
          cards.remove(11)
          cards.append(1)
     return sum(cards
                )





def compare(user_score,computer_score):
     if user_score==computer_score:
          return "Draw 😏"  
     elif computer_score==0:
          return "Lose, opponent has a blackjack😒"
     elif user_score==0:
          return "Win, you has blackjack😁"
     elif user_score>21:
          return "lose😒"
     elif computer_score>21:
          return "win😁"
     elif user_score>computer_score:
          return "win😁"
     else:
          return "lose😒"
          
          
          
def play_game():
     user_cards=[]
     computer_cards=[]

     user_score=-1
     computer_score=-1

     is_game_over= False
     for _ in range(2):
         user_cards.append(deal_card())
         computer_cards.append(deal_card())
     while not is_game_over:
         user_score=calculate_score(user_cards)
         computer_score=calculate_score(computer_cards)
         print(f'Your cards:{user_cards}, current score :{user_score}')
         print(f"computers first cards:{computer_cards[0]}")

         if (computer_score or user_score)==0 or user_score>21:
             is_game_over=True
       
         else:
            choice=input("If you want to draw another card Type 'y' or 'n' :")    
            if choice=='y':
                user_cards.append(deal_card())
            else:
                is_game_over=True  
 
     while computer_score!=0 and computer_score>17:
         computer_cards.append(deal_card())
         computer_score=calculate_score(computer_cards)


     print(f"Your final hand : {user_cards} , final score : {user_score}")
     print(f"Computers final hand :{computer_cards} , final score :{computer_score}")
     print(compare(user_score,computer_score))
     


while input("Do ypu want to play the game  of Blackjack? type y or n :")=='y':
    
     play_game()


     

 
