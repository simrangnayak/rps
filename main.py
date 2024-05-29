from random import randint

# Options that user and computer can choose
options = ['rock', 'paper', 'scissors']

# Winning choice for each index of options list
winners = ['paper', 'scissors', 'rock']

# Losing choice for each index of options list
losers = ['scissors', 'rock', 'paper']

# Keeping track of games won
n_ties = 0
n_user = 0
n_computer = 0

# To ensure that the loop goes on forever
while True:
    # User choice
    player = input('Enter rock, paper, or scissors:')

    # Computer choice
    c_idx = randint(0,2)
    computer = options[c_idx]

    # Raise error if player has not entered rock, paper, or scissors
    if player not in options:
        raise ValueError('Not entered rock, paper, or scissors.')
    
    # Deciding if tie, user, or computer win
    if player == computer:
        print("You chose " + str(player) + " while computer chose " + str(computer) + ". It's a tie!")
        n_ties += 1
    elif player == winners[c_idx]:
        print("You chose " + str(player) + " while computer chose " + str(computer) + ". You win!")
        n_user += 1
    elif player == losers[c_idx]:
        print("You chose " + str(player) + " while computer chose " + str(computer) + ". Computer wins!")
        n_computer += 1

    # Break if player wants to end game
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != 'y':
        break

# Print the number of total ties, number of games user won, and number of games computer won.
print("There were " + str(n_ties) + " tie(s), you won " + str(n_user) + " game(s), and the computer won " + str(n_computer) + " game(s).")