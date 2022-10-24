#rock paper Scissorts Game--

#Imports and variables
import random
global rps_table
global game_map
comp_score = 0
player_score = 0
game_count = 0

#Dictionary for moves and number
game_map = {0:"Rock", 1:"Paper", 2:"Scissors"}

#win-lose matrix
rps_table = [[-1,1,0],[1,-1,2],[0,2,1]]

#game rules
def RPS_instructions():
    print()
    print("Instrctions for Rock-Paper-Scissors")
    print()
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print("type 'H' for (help) if you ever need to review the rules agian!")
    print()

#game loop
while True:
    print()
    Q = input('Do you want to play Rock, Paper, Scissors..?(Y/N) ').lower()
    if Q == 'y':
        print("lets play!")
        if game_count == 0:
            RPS_instructions()
        game_count += 1
    elif Q == 'n':
        if game_count == 0:
            print("Okay, bye!")
        elif game_count != 0:
            if player_score > comp_score:
                print(f"You beat the computer {player_score}-{comp_score} (out of {game_count})games!")
                print("Well done!")
            elif player_score == comp_score:
                print(f"You tied the computer {player_score}-{comp_score} (out of {game_count}) games!")
                print("Good game!")
            else:
                print(f"The computer beat you {comp_score}-{player_score} (out of {game_count}) games!")
                print("Better luck next time!")
                break
        break
    else:
        print("Wrong choice!")
        continue

    print()

    #player input
    print()
    print("Rock (R), Paper (P), Scissors (S), Shoot.....")
    A = input("Enter your move: ")
    if A.lower() == "h":
        RPS_instructions()
        game_count -= 1
        continue
    elif A.lower() == "r":
        player_move = 0
    elif A.lower() == "p":
        player_move = 1
    elif A.lower() == "s":
        player_move = 2
    else:
        print("Please type 'R, 'P', or 'S'")
        game_count -= 1
        continue

        #computer move
    comp_move = random.randint(0,2)
    print("Computer chose",game_map[comp_move].upper())

    #Find the winner
    winner = rps_table[player_move][comp_move]
    if winner == player_move:
        player_score +=1
        print("You win!")
        print("Rounds:",game_count)
    elif winner == comp_move:
        comp_score +=1
        print("Computer wins!")
        print("Rounds:", game_count)
    else:
        print("Tied game!")
        print("Rounds:", game_count)









