from _thread import lock


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

def into_cave():
    print()
    print("you go deeper into the cave and see two tunnels")
    print("to the 'e' tunel goes to the left, the 'w' goes to the right ")
    print("which way do you want to go")

    go = which_direction(['e', 'w'])

    if go == 'e':
        open_cavern()

    if go == 'w':
        dead_end()

def open_cavern():
    print()
    print("You see an open cavern with three paths")
    print("first path goes to the 'e', second path goes 'n', and the tird goes 'w'")
    print("which way do you want to go")

    go = which_direction(['e', 'w', 'n'])

    if go == 'e':
        open_cavern()

    if go == 'n':
        ladder_room()

    if go == 'w':
        vault_room()

def dead_end():
    print()
    print("you find two keys and an open chest")
    print("what do you want to do?")

    (noun, verb) = player_action (['e'], ['key1', 'key2', 'chest' ])

    if verb == "take":
        if noun == "key1":
            print("you have found the vault key")

    if verb == "take":
        if noun == "key2":
            print("you have found the trap_door key")

    if verb == "look":
        if noun == "chest":
            print("you find an axe")

    if verb == "take":
        if noun == "axe":
            print("you take the axe")

    go = which_direction(['e',])

    if go == 'e':
        into_cave()

def ladder_room():
    print()
    print("you look up and see a lock on a trap door")
    print("do you want to unlock the door")

    (noun, verb) = player_action (['u'], ['lock'])

    if verb == "unlock with key2":
        if noun == "lock":
            print("you have unlocked the trap door")
    go = which_direction(['u'])

    if go == 'u':
        dungeon()

def vault_room():
    print()
    print("you find the vault")
    print("do you want to unlock the door")

    (noun, verb) = player_action (['n'], ['lock'])

    if verb == "unlock with key1":
        if noun == "lock":
            print("you unlock the vault")
            print("you freed the death trap ooz")
            print(" the ooz slices you . Game Over!")

def dungeon():
    print()
    print("you see old cells empty")
    print("infont of you is a stair case leading up to the main level")
    print("do you go back or go forward")

    go = which_direction(['s', 'n'])

    if go == 's':
        ladder_room()

    if go == 'n':
        main_level()

def main_level():
    print()
    print("you are spotted by the litch king")
    print("do you wish to attack the litch king")

    (noun, verb) = player_action ()

    if verb == "attack":
        if noun == "litch king":
            print("you have slain the litch king. YOU WIN!!!!")

def worn_path():
    print()
    print("you are at the worn path")
    print(" a bolder falls onto you")
    print("game over")

def forest():
    print()
    print("you stand at the entrance of the forest")
    print("to the south is a small_pond, to the east is a denser_thicket, to the north is an old_fort")
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

    (noun, verb) = player_action (['n', 'e'] ['key'])

    if verb == 'take':
        if noun == 'key':
            print("you take the key")

    go = which_direction(['n'])

    if go == 'n':
        forest()

def denser_thicket():
    print()
    print("you enter the thicket")
    print("a goblin attacks")

    (noun, verb) = player_action (['n', 'e'] ['spear', 'sword', 'mace'])

    if verb == "attack":
        if noun == "Goblin":
            print("you kill the goblin")
            print("which way do you want to go" )
            print("to the east is back to forest, to the north is the old fort, and to the west is a clearing.")

    go = which_direction(['n', 'e', 'w'])

    if go ==  'n':
        old_fort()

    if go == 'e':
        forest()

    if go == 'w':
        clearing()

def clearing():
    print()
    print("you find yourself in a clearing. a spike pit opens up under you")
    print("you fell onto the spikes. Game Over!")

def old_fort():
    print()
    print("your at the gate of the old fort")
    print("the gate is bared but to the west is the side gate")
    print("to the east is a small gap between the stones")
    print("do you clime the gap or go to the door")

    go = which_direction( ['w', 'e'])

    if go == 'w':
        side_gate()

    if go == 'e':
        stone_gap()

def stone_gap():
    print()
    print("would you like to try to climb the stone or go back")

    go = which_direction(['w', 'n'])

    if go == 'w':
        old_fort()

    if go == 'n':
        stone_gap()
        print("you are now crushed under one of the lose stones. Game Over!")


def side_gate():
    print()
    print("the side gate is locked")
    print(" do you unlock the door or go back to the front gate")

    (noun, verb) = player_action (['e', 'n'] ['key'])

    if verb == "unlock":
        if noun == "key":
            print("you unlock the side gate.")
            print("you enter the courtyard and see the remains of an old camp")


    go = which_direction([ 'e', 'n'])

    if go == 'e':
        old_fort()

    if go == 'n':
        old_camp()

def old_camp():
    print()
    print("the old camp is abandoned.")
    print("you see the old chapel to the north")
    print("do you go in, or back out the gate?")

    go = which_direction(['n','s'])

    if go == 's':
        side_gate()

    if go == 'n':
        old_chapel()

def old_chapel():
    print()
    print("the chapel doors creek open")
    print("you find a ancient sword")
    print("do you take the sword")

    (noun, verb) = player_action (['s'], ['ancient sword'])

    if verb == 'take':
        if noun == 'ancient sword':
            print("you have the anceint sword")

    go = which_direction(['s'])

    if go == 's':
        old_camp()


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
open_cavern()
ladder_room()
dungeon()
vault_room()
dead_end()
worn_path()
forest()
small_pond()
denser_thicket()
old_fort()
side_gate()
old_camp()
stone_gap()
clearing()
swamp()