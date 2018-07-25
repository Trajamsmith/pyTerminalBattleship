import random

##---------------------------FUNCTIONS----------------------------------


def create_space_list():
    space_list = []
    
    for i in range(100):
        space_list.append([i, None])
    return space_list




def print_board(space_list):

    print "    A   B   C   D   E   F   G   H   I   J"
    print
    for i in range(10):
        print str(i) + "   ",
        for j in range(10):
            if space_list[10 * i + j][1] == 'hit':
                print "X   ",
            elif space_list[10 * i + j][1] == 'missed':
                print "O   ",
                
            ## Shows you where the computer places its ships
##            elif space_list[10 * i + j][1] == 'generic ship':
##                print "G   ",
##            elif space_list[10 * i + j][1] == 'patrol boat':
##                print "P   ",
##            elif space_list[10 * i + j][1] == 'destroyer':
##                print "D   ",
##            elif space_list[10 * i + j][1] == 'submarine':
##                print "S   ",
##            elif space_list[10 * i + j][1] == 'battleship':
##                print "B   ",
##            elif space_list[10 * i + j][1] == 'aircraft carrier':
##                print "A   ",
                
            else:
                print "    ",
        print
        print




def fire_cannon(space_list):
    success = False
    column_dict = {'A':0, 'B':1,'C':2,'D':3,'E':4,
                   'F':5, 'G': 6, 'H': 7, 'I':8, 'J':9}
    
    while not success:
        column = column_dict.get(input("Fire on what column?: "))
        row = int(input("Fire on what row?: "))

        current_attack = (row * 10) + column
        is_it_hit = does_it_hit(space_list, current_attack)
        if space_list[current_attack][1] == 'hit' or\
             space_list[current_attack][1] == 'missed':
            print 
            print "You've already fired at that location."
            print 
            sucess = False
        elif is_it_hit:
            space_list[current_attack][1] = 'hit'
            print 
            print "You hit the enemy ship!"
            print 
            success = True
        else:
            space_list[current_attack][1] = 'missed'
            print 
            print "You missed the enemy's ships..."
            print 
            success = True




def does_it_hit(space_list, current_attack):

    if space_list[current_attack][1] == None:
        return False
    else:
        return True



def game_over(space_list, turns, max_turns):
    remaining_ship_spaces = 0
    
    for i in range(len(space_list)):
        if space_list[i][1] == "generic ship" or\
           space_list[i][1] == "patrol boat" or\
           space_list[i][1] == "destroyer" or\
           space_list[i][1] == "submarine" or\
           space_list[i][1] == "battleship" or\
           space_list[i][1] == "aircraft carrier":
            remaining_ship_spaces += 1
            
    if remaining_ship_spaces > 0 and turns < max_turns:
        return False
    
    elif turns >= max_turns:
        print 
        print "The enemy's sunk all your battleships."
        print "Thank you for playing!"
        return True

    else:
        print 
        print "You've won the game!"
        return True



##----------------------------class Ship()----------------------------------


class Ship():

    def __init__(self):
        self.boat_length = 0
        self.baot_name = "generic ship"



    ## Use this method rather than auto_add_ship_to_board to add ships manually
    def add_ship_to_board(self, space_list):
        success = False
        
        while not success:
            boat_location = int(input("Where should I put the %s? "
                                      % self.boat_name))
            orientation = input("Orient the boat vertically or horizontally? ")

        ## Setting values such that the user can't put in a boat_location
        ## that would cause the boat to go off the map
            max_hor_boat_pos = (boat_location + self.boat_length) % 10
            max_vert_boat_pos = boat_location + self.boat_length * 10

        ## Replaces the empty values in the space list to reflect the ship's
        ## horizontal orientation, hence += 1
            if orientation == 'horizontally' and \
               max_hor_boat_pos > (boat_location % 10):
                for i in range(self.boat_length):
                    space_list[boat_location][1] = self.boat_name
                    boat_location += 1
                    success = True

        ## Replaces the empty values in the space list to reflect the ship's
        ## horizontal orientation, hence += 10
            elif orientation == 'vertically' and max_vert_boat_pos < 100:
                for i in range(self.boat_length):   
                    space_list[boat_location][1] = self.boat_name
                    boat_location += 10
                    success = True

            else:
                print 
                print "That boat cannot go there."
                print 
                success = False



    ## Same as above, but automated rather than user-input
    def auto_add_ship_to_board(self, space_list):
        success = False
    
        while not success:
            boat_location = random.randrange(0,100)
            orientation = random.randrange(0,2)

            max_hor_boat_pos = (boat_location + self.boat_length) % 10
            max_vert_boat_pos = boat_location + self.boat_length * 10

            boat_overlap = self.boat_overlap(space_list, boat_location, orientation)

            if not boat_overlap:
                if orientation == 0 and \
                   max_hor_boat_pos > (boat_location % 10):
                    for i in range(self.boat_length):
                        space_list[boat_location][1] = self.boat_name
                        boat_location += 1
                    success = True

                elif orientation == 1 and max_vert_boat_pos < 100:
                    for i in range(self.boat_length):   
                        space_list[boat_location][1] = self.boat_name
                        boat_location += 10
                    success = True

            else:
                success = False



    def boat_overlap(self, space_list, boat_location, orientation):
        overlap_counter = 0
        boat_check_loc = boat_location
        
        ## Check horizontal overlap
        if orientation == 0:
            for i in range(self.boat_length):
                if boat_check_loc < 100 and\
                    space_list[boat_check_loc][1] != None:
                    overlap_counter += 1
                boat_check_loc += 1

        ## Check vertical overlap
        if orientation == 1:
            for i in range(self.boat_length):
                if boat_check_loc < 100 and\
                    space_list[boat_check_loc][1] != None:
                    overlap_counter += 1
                boat_check_loc += 10

        if overlap_counter > 0:
            return True

        else:
            return False

                        

##-----------------------------SHIP SUBCLASSES------------------------------

class Patrol_boat(Ship):

    def __init__(self):
        self.boat_length = 2
        self.location = (-1,-1)
        self.boat_name = 'patrol boat'



class Destroyer(Ship):

    def __init__(self):
        self.boat_length = 3
        self.location = (-1,-1)
        self.boat_name = 'destroyer'



class Submarine(Ship):

    def __init__(self):
        self.boat_length = 3
        self.location = (-1,-1)
        self.boat_name = 'submarine'



class Battleship(Ship):

    def __init__(self):
        self.boat_length = 4
        self.location = (-1,-1)
        self.boat_name = 'battleship'



class Aircraft_carrier(Ship):

    def __init__(self):
        self.boat_length = 5
        self.location = (-1,-1)
        self.boat_name = 'aircraft carrier'

