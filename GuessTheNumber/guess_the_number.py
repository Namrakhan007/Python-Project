#Number Guessing Game 
import random

logo = """
  ____  __ __    ___  _____ _____     ______  __ __    ___      ____   __ __  ___ ___  ____     ___  ____  
 /    ||  |  |  /  _]/ ___// ___/    |      ||  |  |  /  _]    |    \ |  |  ||   |   ||    \   /  _]|    \ 
|   __||  |  | /  [_(   \_(   \_     |      ||  |  | /  [_     |  _  ||  |  || _   _ ||  o  ) /  [_ |  D  )
|  |  ||  |  ||    _]\__  |\__  |    |_|  |_||  _  ||    _]    |  |  ||  |  ||  \_/  ||     ||    _]|    / 
|  |_ ||  :  ||   [_ /  \ |/  \ |      |  |  |  |  ||   [_     |  |  ||  :  ||   |   ||  O  ||   [_ |    \ 
|     ||     ||     |\    |\    |      |  |  |  |  ||     |    |  |  ||     ||   |   ||     ||     ||  .  \
|___,_| \__,_||_____| \___| \___|      |__|  |__|__||_____|    |__|__| \__,_||___|___||_____||_____||__|\_|
                                                                                                           """
print(logo)
print("welcome to the number geussing game!")
print("I'm thinking of number 1 to 100")

turns = 0
lst = list(range(1, 101))
number = random.choice(lst)
print(number)

ELT = 10
HLT = 5


def difficulty():
    level = input("Choose a difficulty. Type 'easy or 'hard':")
    if level == "easy":
        return ELT
    else:
        return HLT

    
def game():

    def check_ans(user, number, turns):
        if user > number:
            print("Too High.")
            return turns - 1
        elif user < number:
            print("Too Low")
            return turns - 1
        else:
            print(f"gotcha! the answer was {number}")

    

    turns = difficulty()
    
    user = 0
    while user != number:
        print(f"you have {turns} attempts remaining to guess the number.")
        user = int(input("guess the number:"))
        
        
        turns = check_ans(user, number, turns)
        if turns == 0:
            print("you ran out of attempts so you lost!")
            break
        elif user != number:
            print("guess again")
            
game()
