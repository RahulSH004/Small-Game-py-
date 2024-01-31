#ROCK PAPER SCISSORS
import random

def print_rock():
    rock = """
    Rock
    -------
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """
    print(rock)

def print_paper():
    paper = """
    Paper
    -------
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    """
    print(paper)

def print_scissors():
    scissors = """
    Scissors
    -------
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
    print(scissors)

def get_user_choice():
    user_choice = int(input("ENTER YOUR CHOICE : "))
    while user_choice not in [0 , 1, 2]:
        print("invalid choice , YOU LOSE !!")
        user_choice = int(input("ENTER YOUR CHOICE : "))
        
    return user_choice

def get_comp_choice():
    return random.randint(0,2)

def get_winner(user_choice,comp_choice):
    if user_choice == comp_choice:
        return "IT'S A TIE"
    elif (
        
        (user_choice == 0 and comp_choice == 1) or
        (user_choice == 2 and comp_choice == 0) or
        (user_choice == 1 and comp_choice == 2)
    ):    
        return "YOU WIN !! HURRAYY!!"
    else:
        return "YOU LOSE !! LOL"
    
if __name__=="__main__":
    
    print("_____WELCOME TO ROCK PAPER SCISSOR GAME_____")
    print("---INSTRUCTION---")
    print("   ROCK --> 0")
    print("   SCISSORS --> 1")
    print("   PAPER --> 2")
    print("-----NOW YOU CAN PLAY-----")
    
    user_choice = get_user_choice()
    computer_choice = get_comp_choice()
    print("\nYOUR CHOICE:")
    if user_choice == 0:
        print_rock()
    elif user_choice == 1:
        print_scissors()
    elif user_choice == 2:
        print_paper()

    
    print("\nCOMPUTER CHOICE : ")
    
    if computer_choice == 0:
        print_rock()
    elif computer_choice == 1:
        print_scissors()
    elif computer_choice == 2:
        print_paper()
    
    result = get_winner(user_choice,computer_choice)
    print(result)