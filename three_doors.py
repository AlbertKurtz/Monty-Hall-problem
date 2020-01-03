import numpy.random
import random
import matplotlib.pyplot as plt

def create_doors():
    doors = {1 : None, 2: None, 3 : None}

    car_door = numpy.random.randint(1,4)
    goat_doors = [i for i in range(1,4) if i!= car_door]

    doors[car_door] = True
    for door in goat_doors:
        doors[door] = False
    return doors

def choice(n, doors):
    
    if doors[n]:
        doors.pop(n)       
        open_goat_door = random.choice(list(doors.keys()))
        doors.pop(open_goat_door)
        other_door = list(doors.keys())[0]
        
    else:
        doors.pop(n)
        open_goat_door = [key for key,value in doors.items() if not value][0]
        doors.pop(open_goat_door)
        other_door = list(doors.keys())[0]
        
    return n, other_door

keep_door = []
change_door = []

number_of_games = 1000000

for _ in range(number_of_games):
    doors = create_doors()
    doors_copy = doors.copy()
    player_choice = numpy.random.randint(1,4)
    keep, change = choice(player_choice, doors_copy)

    keep_door.append(doors[keep])
    change_door.append(doors[change])

print("In {} games:".format(number_of_games))
print("Not switching door lead to {} winnings".format(sum(keep_door)))
print("Switching door lead to {} winnings".format(sum(change_door)))



    
