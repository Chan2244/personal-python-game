from game_art import (display_weapons_shop_art, display_welcome_art, display_entrance_art, \
    display_armor_shop_art, display_main_gate_art, display_mountain_art, display_cave_art, \
    display_into_cave_art, display_open_cavern_art, display_dead_end_art, display_ladder_room_art,\
    display_vault_room_art, display_dungeon_art, display_main_level_art, display_worn_path_art, display_forest_art,\
    display_small_pond_art, display_denser_thicket_art, display_clearing_art, display_old_fort_art, display_stone_gap_art,\
    display_side_gate_art, display_old_camp_art, display_old_chapel_art, display_swamp_art)

from end_game import display_end_game_function

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

  global verb, noun
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
    display_welcome_art()

    player = input("What's your name adventurer?")
    print("Welcome to Evernight,", player)



def entrance():
    display_entrance_art()
    print()
    print("you stand before the town square")
    print("to the east is a weapons shop")
    print("to the west is a armor shop")
    print("the main gate is to the south")

    go = which_direction(['w', 'a', 'g'])

    if go == "w":
        weapons_shop()

    if go == 'a':
        armor_shop()

    if go == 'g':
        main_gate()

def weapons_shop():
    display_weapons_shop_art()
    print()
    print("you look and see a sword, spear, mace. and trident")
    print("which do you pick")
    print("to exit shop go west")

    items = ['sword', 'spear', 'mace', 'axe', 'trident']
    (verb, noun) = player_action(['e'], items)
    if verb == "go":
        if noun == 'e':
            entrance()

    if verb == "take":
        if noun in items:
            print(f"you have chosen to take the {noun} ")

    go = which_direction(['w'])

    if go == 'w':
        entrance()



def armor_shop():
    display_armor_shop_art()
    print()
    print("you look and see leather, chainmail, plate, wooden shield, steel shield,")
    print("which do you pick")
    print("to exit shop go east")

    items = ['leather', 'chainmail', 'plate', 'wooden_shield', 'steel_shield']
    (verb, noun) = player_action(['e'], items)
    if verb == "go":
        if noun == 'e':
            entrance()

    if verb == "take":
        if noun in items:
            print(f"you have chosen to take the {noun} armor")


    go = which_direction(['e'])

    if go == 'e':
        entrance()

def main_gate():
    display_main_gate_art()
    print()
    print("you stand at the main gate")
    print("to the east a path leads to the mountain")
    print("to the west leads to the forest")
    print("to the south leads you into a swamp")

    go = which_direction(['m', 'f', 's'])

    if go == 'm':
        mountain()

    if go == 'f':
        forest()

    if go == 's':
        swamp()

def mountain():
    display_mountain_art()
    print()
    print("you stand at the base of the mountain")
    print(" to the north is a cave, to the south is a open well worn path")
    print("what do you want to do?")

    go = which_direction(['c', 'w'])

    if go == 'c':
        cave()

    if go == 'w':
        worn_path()

def cave():
    display_cave_art()
    print()
    print("your at the entrance of the cave")
    print("you see a wolf")
    print("what do you do")

    (verb, noun) = player_action (['n'])

    if verb == "attack":
        if noun == "wolf":
            print("you kill the wolf. which way do you want to go.")
            print(" 'n' goes into the cave.  's' goes back to the mountain.")

    go = which_direction(['i', 'm'])
    if go == 'i':
        into_cave()

    if go == 'm':
        mountain()

def into_cave():
    display_into_cave_art()
    print()
    print("you go deeper into the cave and see two tunnels")
    print("to the 'e' tunel goes to the left, the 'w' goes to the right ")
    print("which way do you want to go")

    go = which_direction(['l', 'r'])

    if go == 'l':
        open_cavern()

    if go == 'r':
        dead_end()

def open_cavern():
    display_open_cavern_art()
    print()
    print("You see an open cavern with three paths")
    print("first path goes to the 'e', second path goes 'n', and the tird goes 'w'")
    print("which way do you want to go")

    go = which_direction(['f', 's', 't'])

    if go == 'f':
        open_cavern()

    if go == 's':
        ladder_room()

    if go == 't':
        vault_room()

def dead_end():
    display_dead_end_art()
    print()
    print("you find two keys and an open chest")
    print("what do you want to do?")

    items = ['key1', 'key2', 'chest',]
    (verb, noun) = player_action(['e'], items)
    if verb == "go":
        if noun == 'e':
            entrance()

    if verb == "take":
        if noun in items:
            print(f"you have chosen to take the {noun} ")

    go = which_direction(['e',])

    if go == 'e':
        into_cave()

def ladder_room():
    display_ladder_room_art()
    print()
    print("you look up and see a lock on a trap door")
    print("do you want to unlock the door")

    (verb, noun) = player_action (['u'], ['lock'])

    if verb == "unlock with key2":
        if noun == "lock":
            print("you have unlocked the trap door")
    go = which_direction(['u'])

    if go == 'u':
        dungeon()

def vault_room(current_room=None):
    display_vault_room_art()
    display_end_game_function(current_room = current_room)
    print()
    print("you find the vault")
    print("do you want to unlock the door")

    (verb, noun) = player_action (['n'], ['lock'])

    if verb == "unlock with key1":
        if noun == "lock":
            print("you unlock the vault")
            print("you freed the death trap ooz")
            print(" the ooz slices you . Game Over!")

def dungeon():
    display_dungeon_art()
    print()
    print("you see old cells empty")
    print("in font of you is a stair case leading up to the main level")
    print("do you go back or go forward")

    go = which_direction(['b', 'f'])

    if go == 'b':
        ladder_room()

    if go == 'f':
        main_level()

def main_level():
    display_main_level_art()
    print()
    print("you are spotted by the litch king")
    print("do you wish to attack the litch king")

    (verb, noun) = player_action (['attack'], ['litch king'])

    if verb == "attack":
        if noun == "litch king":
            print("you have slain the litch king. YOU WIN!!!!")

def worn_path(current_room = None):
    display_worn_path_art(current_room = current_room)
    display_end_game_function()
    print()
    print("you are at the worn path")
    print(" a bolder falls onto you")
    print("game over")

def forest():
    display_forest_art()
    print()
    print("you stand at the entrance of the forest")
    print("to the south is a small_pond, to the east is a denser_thicket, to the north is an old_fort")
    print("what do you want to do?")

    go = which_direction(['s', 'd', 'o'])

    if go == 'o':
        old_fort()

    if go == 'd':
        denser_thicket()

    if go == 's':
        small_pond()

def small_pond():
    display_small_pond_art()
    print()
    print("you stand at the edge of the small pond")
    print("you find a key")


    (verb, noun) = player_action (['n', 'e'], ['key'])

    if verb == 'take':
        if noun == 'key':
            print("you take the key")

    go = which_direction(['n'])

    if go == 'n':
        forest()

def denser_thicket():
    display_denser_thicket_art()
    print()
    print("you enter the thicket")
    print("a goblin attacks")

    (verb, noun) = player_action (['n', 'e'],  ['Goblin'])

    if verb == "attack":
        if noun == "Goblin":
            print("you kill the goblin")
            print("which way do you want to go" )
            print("to the east is back to forest, to the north is the old fort, and to the west is a clearing.")

    go = which_direction(['f', 'o', 'c'])

    if go ==  'o':
        old_fort()

    if go == 'f':
        forest()

    if go == 'c':
        clearing()

def clearing(current_room = None):
    display_clearing_art()
    display_end_game_function(current_room = current_room)
    print()
    print("you find yourself in a clearing. a spike pit opens up under you")
    print("you fell onto the spikes. Game Over!")


def old_fort():
    display_old_fort_art()
    print()
    print("your at the gate of the old fort")
    print("the gate is bared but to the west is the side gate")
    print("to the east is a small gap between the stones")
    print("do you clime the gap or go to the door")

    go = which_direction( ['s', 'g'])

    if go == 's':
        side_gate()

    if go == 'g':
        stone_gap()

def stone_gap(current_room = None):
    display_end_game_function(current_room = current_room)
    display_stone_gap_art()
    print()
    print("would you like to try to climb the stone or go back")

    go = which_direction(['y', 'n'])

    if go == 'y':
        old_fort()

    if go == 'n':
        stone_gap()
        print("you are now crushed under one of the lose stones. Game Over!")


def side_gate():
    display_side_gate_art()
    print()
    print("the side gate is locked")
    print(" do you unlock the door or go back to the front gate")

    (verb, noun) = player_action (['e', 'n'], ['gate'])

    if verb == "unlock":
        if noun == "gate":
            print("you unlock the side gate.")
            print("you enter the courtyard and see the remains of an old camp")


    go = which_direction([ 'e', 'n'])

    if go == 'e':
        old_fort()

    if go == 'n':
        old_camp()

def old_camp():
    display_old_camp_art()
    print()
    print("the old camp is abandoned.")
    print("you see the old chapel to the north")
    print("do you go in, or back out the gate?")

    go = which_direction(['o','g'])

    if go == 's':
        side_gate()

    if go == 'n':
        old_chapel()

def old_chapel():
    display_old_chapel_art()
    print()
    print("the chapel doors creek open")
    print("you find a ancient sword")
    print("do you take the sword")

    (verb, noun) = player_action (['s'], ['ancient sword'])

    if verb == 'take':
        if noun == 'ancient sword':
            print("you have the anceint sword")

    go = which_direction(['s'])

    if go == 's':
        old_camp()


def swamp(current_room = None):
    display_swamp_art()
    display_end_game_function( current_room = current_room)
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
old_chapel()

