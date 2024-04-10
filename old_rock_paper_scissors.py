import random

choices = ["Rock", "Paper", "Scissors"]
computer_choice = my_choice = ties = ai_wins = my_wins = 0

print("Welcome to Rock, Paper, Scissors game! Pick one or type Q to quit")
while my_choice != "Q":
    print(f"Your wins: {my_wins}, my wins: {ai_wins}, ties: {ties}")
    my_choice = input("Pick rock, paper or scissors: ").capitalize()
    if my_choice == "Q":
        print(f"Game ended with score:\nYour wins: {my_wins}, my wins: {ai_wins}, ties: {ties}")
        print("Bye! See you soon :)")
    elif my_choice not in choices:
        print("Wrong choice!")
    else:
        computer_choice = random.choice(choices)
        if computer_choice == my_choice:
            print(f"You picked {my_choice} and I also picked {computer_choice}")
            print("That is a tie!")
            ties += 1
        elif computer_choice == "Rock":
            if my_choice == "Paper":
                print(f"You picked {my_choice} and I picked {computer_choice}")
                print("You win!")
                my_wins += 1
            elif my_choice == "Scissors":
                print(f"You picked {my_choice} and I picked {computer_choice}")
                print("You lose!")
                ai_wins += 1
        elif computer_choice == "Paper":
            if my_choice == "Scissors":
                print(f"You picked {my_choice} and I picked {computer_choice}")
                print("You win!")
                my_wins += 1
            elif my_choice == "Rock":
                print(f"You picked {my_choice} and I picked {computer_choice}")
                print("You lose!")
                ai_wins += 1
        elif computer_choice == "Scissors":
            if my_choice == "Rock":
                print(f"You picked {my_choice} and I picked {computer_choice}")
                print("You win!")
                my_wins += 1
            elif my_choice == "Paper":
                print(f"You picked {my_choice} and I picked {computer_choice}")
                print("You lose!!")
                ai_wins += 1
