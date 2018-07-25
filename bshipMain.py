import bshipMethods
import random

space_list = bshipMethods.create_space_list()

patrol_boat = bshipMethods.Patrol_boat()
destroyer = bshipMethods.Destroyer()
submarine = bshipMethods.Submarine()
battleship = bshipMethods.Battleship()
aircraft_carrier = bshipMethods.Aircraft_carrier()

def main():
    print "The computer is setting up its ships..."
    print
    print
    patrol_boat.auto_add_ship_to_board(space_list)
    destroyer.auto_add_ship_to_board(space_list)
    submarine.auto_add_ship_to_board(space_list)
    battleship.auto_add_ship_to_board(space_list)
    aircraft_carrier.auto_add_ship_to_board(space_list)
    bshipMethods.print_board(space_list)

    done = False
    turn = 1
    max_turns = random.randrange(1, 5)
    
    while not done:
        bshipMethods.fire_cannon(space_list)
        bshipMethods.print_board(space_list)
        done = bshipMethods.game_over(space_list, turn, max_turns)
        turn += 1


main()
