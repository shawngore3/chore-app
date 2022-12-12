import utils
import random

def main():
    #ranodmize the names
    names = randomize_dict(utils.names)
    # loop through name dict randomly and use assign_chores to assign chores
    
    for name in names:
        # get the age of the person
        age = names[name]
        # get the min number of chores for the person
        count = chore_count(age)
        # assign the chores
        assigned_chores = assign_chores(count)
        # print out the name and the chores
        print(f"{name} has {len(assigned_chores)}: ")
        for chore in assigned_chores:
            print (chore)
        print()
    
    



#fucntion that takes name and age and returns chore count
def chore_count(age):
    if age > 13:
        return 6
    if age > 11:
        return 5
    return 4

#function that takes chore count and returns a dict of random chores and removes it from the chore dict
def assign_chores(count):
    chores = []
    while len(utils.chores) > 0 and len(chores) < count:
        random_chore = random.choice(list(utils.chores.keys()))
        chores.append(random_chore)
        # if chore name contains Sweep but not Mop, add mop to the list
        if "Sweep" in random_chore and "Mop" not in random_chore:
            chores.append("Mop")
        utils.chores.pop(random_chore)
    return chores
        
#function that takes a dict and returns a random dict
def randomize_dict(dict):
    random_dict = {}
    while len(dict) > 0:
        random_key = random.choice(list(dict.keys()))
        random_dict[random_key] = dict[random_key]
        dict.pop(random_key)
    return random_dict


main()