import World
from players import Player


def play(): #creating game play
    World.load_tiles() #load the tiles from the World.py
    player = Player()
    room = World.tile_exists(player.location_x, player.location_y) #if the tile exists
    print(room.intro_text()) #print the intro text
    while player.is_alive() and not player.victory:
        room = World.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break

if __name__ == "__main__":
    play() # play the game