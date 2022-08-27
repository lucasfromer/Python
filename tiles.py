import items, Enemies, actions, World


class MapTile: # create MapTile object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self): #define intro text
        """Information to be displayed when the player moves into this tile."""
        raise NotImplementedError()

    def modify_player(self, the_player): # Define modify player
        """Process actions that change the state of the player."""
        raise NotImplementedError()

    def adjacent_moves(self): #define moving throughout the map
        """Returns all move actions for adjacent tiles."""
        moves = []
        if World.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if World.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if World.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if World.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self): #define available actions
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves

class Apartment(MapTile): #starting point for this story
    def intro_text(self):
        return """
        You find yourself on a journey to find your true calling.
        At this point in the quest you're taking damage from your Ex and Life.
        You must find the key while battling your way through this. 
        """

    def modify_player(self, the_player):
        #Room has no action on player
        pass

class EmptyRoad(MapTile): #empty road room
    def intro_text(self):
        return """
        You leave the apartment and head OutInTown.
        """

    def modify_player(self, the_player):
        #Room has no action on player
        pass

class OutInTown(MapTile): # out in town room
        def __init__(self, x, y):
            super().__init__(x, y)
    
        def intro_text(self):
            return """
            When your out in town, you're out celebrating your birthday
            you meet a friend who at that time, you didn't realize
            would be a big role in your life.
            """    
        def modify_player(self, the_player):
            #Room has no action on player
            pass

class EnemyRoom(MapTile): #enemy room definition
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
class ExSpouseRoom(EnemyRoom): 
    def __init__(self, x, y):
        super().__init__(x, y, Enemies.Ex_Spouse())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You've encountered your Spouse who is accusing you of things
            that you did not do despite no matter what you say. You have a choice, Stay or Leave.
            """

        else:
            return """The bridge between you and your Spouse is finished."""

    def modify_player(self, the_player):
        #Room has no action on player
        pass

class FindKeyRoom(OutInTown): #Key room definition
    def __init__(self, x, y):
        super().__init__(x, y)

    def intro_text(self):
        return """
        After getting to know the knight you noticed back when you and your Spouse
        were out celebrating, he introduced you to what you found was the key to unlocking
        true happiness.
        """

class LeaveApartment(MapTile): #victory room
    def intro_text(self):
        return """
        You decide to make your own life without all the damage from your Ex.
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True
