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
    print("you look and see a sword, spear, mace, and bow with arrows")
    print("which do you pick")
    print("to exit shop go west")

    (verb, noun) = player_action (['s'], ['sword', 'mace', 'bow and arrows', 'spear'])
    if verb == "go":
        if noun[0] == 'w':
            entrance()

        if verb == "take":
            if noun[0] == "sword":
                print("you have chosen to take the sword")

        if verb == "take":
            if noun[0] == "mace":
                print("you have chosen to take the mace")

        if verb == "take":
            if noun[0] == "bow and arrows":
                print("you have chosen to take the bow and arrows")

        if verb == "take":
            if noun[0] == "spear":
                print("you have chosen to take take the spear")

        if verb == "exit":
            if noun[0] == "exit choice":
                print("you exit the weapon selection")

    go = which_direction(['w'])

    if go == 'w':
        entrance()


def armor_shop():
    print()
    print("you look and see leather, chainmail, plate, wooden shield, steel shield,")
    print("which do you pick")
    print("to exit shop go east")

    (verb, noun) = player_action(['e'], ['leather', 'chainmail', 'plate', 'wooden shield', 'steel shield'])
    if verb == "go":
        if noun[0] == 'e':
            entrance()

        if verb == "take":
            if noun[0] == "leather":
                print("you have chosen to take the leather armor")

        if verb == "take":
            if noun[0] == "chainmail":
                print("you have chosen to take the chainmail armor")

        if verb == "take":
            if noun[0] == "plate":
                print("you have chosen to take the plate armor")

        if verb == "take":
            if noun[0] == "wooden shield":
                print("you have chosen to take take the wooden shield")

        if verb == "take":
            if noun[0] == "steel shield":
                print("you have chosen to take the steel shield")

        if verb == "exit":
            if noun[0] == "exit choice":
                print("you exit the weapon selection")

    go = which_direction(['w'])

    if go == 'w':
        entrance()

def main_gate():
    print()
    print("you stand at the main gate")
    print("")


welcome()
entrance()
weapons_shop()
armor_shop()
main_gate()







