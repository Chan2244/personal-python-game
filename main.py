def which_direction(choices):

    while True:
        c = ",".join(choices)
        go = input("Which way do you want to go: " + c +"? ")
        if go == "": continue
        go = go[0].lower()
        if go in choices:
            return go
        else:
            print("I don't understand")

def player_action(directions, objects):

  while True:
    c = input("What do you want to do? ")
    try:
      (verb, noun) = c.lower().split(" ")
    except ValueError:
      print("I don't understand")
      continue

    if verb == "go":
      if noun[0] in directions: break
      else: print("You can't go in direction", noun)
    elif verb == "take":
      if noun in objects: break
      else: print("There is no", noun, "to take")
    else:
      print("I only understand two commands: go, take")

  return verb, noun

def welcome():
    player = input("What's your name adventurer?")
    print("Welcome to Evernight,", player)

def entrance():
    print()
    print("you stand before the town square")
    print("to the east is a weapons shop")
    print("to the west is a armor shop")
    print("the main gate is to the south")

    go = which_direction(['e', 'w', 's'])

    if go == "e":
        weapons_shop()

    if go == 'w':
        armor_shop()

    if go == 's':
        main_gate()

def weapons_shop():
    print()
    print("you look and see a sword, spear, mace.")
    print("which do you pick")
    print("to exit shop go west")

    (verb, noun) = player_action (['s'], ['sword', 'mace', 'spear'])
    if verb == "go":
        if noun == 'w':
            entrance()

    if verb == "take":
        if noun == "sword":
            print("you have chosen to take the sword")

    if verb == "take":
        if noun == "mace":
            print("you have chosen to take the mace")

    if verb == "take":
        if noun == "spear":
            print("you have chosen to take take the spear")

    if verb == "exit":
         if noun == "exit choice":
            print("you exit the weapon selection")

    go = which_direction(['w'])

    if go == 'w':
        entrance()


def armor_shop():
    print()
    print("you look and see leather, chainmail, plate, wooden shield, steel shield,")
    print("which do you pick")
    print("to exit shop go east")

    (verb, noun) = player_action(['e'], ['leather', 'chainmail', 'plate', 'wooden_shield', 'steel_shield'])
    if verb == "go":
        if noun == 'e':
            entrance()

    if verb == "take":
        if noun == "leather":
            print("you have chosen to take the leather armor")

    if verb == "take":
        if noun == "chainmail":
            print("you have chosen to take the chainmail armor")

    if verb == "take":
        if noun == "plate":
            print("you have chosen to take the plate armor")

    if verb == "take":
         if noun == "wooden_shield":
            print("you have chosen to take take the wooden shield")

    if verb == "take":
        if noun == "steel_shield":
            print("you have chosen to take the steel shield")

    if verb == "exit":
        if noun == "exit choice":
            print("you exit the weapon selection")

    go = which_direction(['e'])

    if go == 'e':
        entrance()

def main_gate():
    print()
    print("you stand at the main gate")
    print("to the east a path leads to the mountain")
    print("to the west leads to the forest")
    print("to the south leads you into a swamp")

    go = which_direction(['e', 'w', 's'])

    if go == 'e':
        mountain()

    if go == 'w':
        forest()

    if go == 's':
        swamp()

def mountain():
    print()
    print("you stand at the base of the mountain")
    print(" to the north is a cave, to the south is a open well worn path")
    print("what do you want to do?")

    go = which_direction(['n', 's'])

    if go == 'n':
        cave()

    if go == 's':
        worn_path()

def cave():
    print()
    print("your at the entrance of the cave")
    print("you see a wolf")
    print("what do you do")

    (noun, verb) = player_action (['n'], ['spear, sword, mace'])

    if verb == "attack":
        if noun == "wolf":
            print("you kill the wolf. which way do you want to go.")
            print(" 'n' goes into the cave.  's' goes back to the mountain.")

    go = which_direction(['n', 's'])
    if go == 'n':
        into_cave()

    if go == 's':
        mountain()

def worn_path():
    print()
    print("you are at the worn path")
    print(" a bolder falls onto you")

def forest():
    print()
    print("you stand at the entrance of the forest")
    print("to the south is a small pond, to the east is a denser thicket, to the north is an old fort")
    print("what do you want to do?")

    go = which_direction(['s', 'e', 'n'])

    if go == 'n':
        old_fort()

    if go == 'e':
        denser_thicket()

    if go == 's':
        small_pond()

def small_pond():
    print()
    print("you stand at the edge of the small pond")
    print("you find a key")
    print("what do you want to do?")

    (noun, verb) = player_action (['n'] ['key'])

    if verb == 'take':
        if noun == 'key':
            print("you take the key")
    go = which_direction(['n'])

    if go == 'n':
        forest()

def denser_thicket():
    print()

def swamp():
    print()
    print("you stand at the edge of the swamp")
    print("you fall in to the quicksand.")
    print("Game Over!")

    

welcome()
entrance()
weapons_shop()
armor_shop()
main_gate()
mountain()
cave()
into_cave()
worn_path()
forest()
smallpond()
denser_thicket()
old_fort()
swamp()