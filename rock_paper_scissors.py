import random


def display_record():
    return 'wins: ' + str(win_count), "losses: " + str(loss_count), "ties: " + str(tie_count)


choices = ["rock", "paper", "scissors"]
win_count = 0
loss_count = 0
tie_count = 0
game_count = 0
round_count = 0
# record = display_record()

print("Welcome to Rock, Paper, Scissors! ")

game_start = input("Would you like to play? (yes/no) ")

if game_start == "yes":
    round_count = int(input("How many rounds would you like to play? "))

    while game_count != round_count:
        cpu_choice = random.choice(choices)
        user_choice = input("Enter your selection (rock/paper/scissors): ").lower()
        print("cpu threw: " + cpu_choice)

        if user_choice in choices:
            if user_choice == choices[0]:
                if cpu_choice == choices[0]:
                    print('It\'s a tie!')
                    tie_count += 1
                elif cpu_choice == choices[1]:
                    print("You lost this round! ")
                    loss_count += 1
                elif cpu_choice == choices[2]:
                    print("You won this round! ")
                    win_count += 1
            elif user_choice == choices[1]:
                if cpu_choice == choices[1]:
                    print('It\'s a tie!')
                    tie_count += 1
                elif cpu_choice == choices[2]:
                    print("You lost this round! ")
                    loss_count += 1
                elif cpu_choice == choices[0]:
                    print("You won this round! ")
                    win_count += 1
            elif user_choice == choices[2]:
                if cpu_choice == choices[2]:
                    print('It\'s a tie!')
                    tie_count += 1
                elif cpu_choice == choices[0]:
                    print("You lost this round! ")
                    loss_count += 1
                elif cpu_choice == choices[1]:
                    print("You won this round! ")
                    win_count += 1
        else:
            print("invalid input. ")

        game_count += 1

    print()

    if win_count > loss_count:
        print("congratulations, you won best 2 out of 3")
    elif win_count == loss_count:
        print("woah, it's a tie!")
    else:
        print("you lost!")

elif game_start == "no":
    print("Maybe next time...")
else:
    print("Invalid input")


