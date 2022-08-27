_World = {}  # creating the World for this text based game
starting_position = (0, 0)

def tile_exists(x, y):
        return _World.get((x, y))

def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    with open('Resources/map.txt', 'r') as f: # opens the map text file created with the room lay out
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')
            if tile_name == 'Apartment':
                global starting_position
                starting_position = (x, y)
            _World[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x,y)
            # gets the attributes from tiles of the tile name in reference to the map and the tiles code
            # to determine which coords match with the map and then your able to move directions

