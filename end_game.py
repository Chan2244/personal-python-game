
def display_end_game_function(current_room,ends_game = True):
    losing_room = ["vault_room","worn_path", "clearing", "stone_gap", "swamp"]
    if current_room in losing_room and ends_game:
        print(f"you entered the" + current_room + "Game Over!!!")
        return True

def victory_function(current_room):
    winning_rooms = ["main_level"]
    if current_room in winning_rooms:
        print("you won the game!!")
        return True

