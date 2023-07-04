import random

user_hands = ['ROCK', 'PAPER', 'SCISSORS']
computer_hands = ['ROCK', 'PAPER', 'SCISSORS']
game_on = True
quit_message = 0

while game_on == True:
    computer_choice = random.randint(0, 2)
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    
    if user_choice >= 3 or user_choice < 0:
        print("What are you tryin' to pull here, buddy?")
        continue
    else:    
        print(f"You chose: {user_hands[user_choice]} and the computer chose: {computer_hands[computer_choice]}")

        if user_choice == 0 and computer_choice == 2:
            print("You win!")
        elif computer_choice == 0 and user_choice == 2:
            print("You lose")
        elif computer_choice > user_choice:
            print("You lose")
        elif user_choice > computer_choice:
            print("You win!")
        elif computer_choice == user_choice:
            print("It's a draw")
        
        quit_message += 1
        play_again = input('Would you like to quit?: (y) (n)')
        if play_again.lower() == 'y':
            print(f"Wow, after only {quit_message} rounds?  You're never going to make it to State.")
            game_on = False
        if play_again.lower() == 'n':
            continue