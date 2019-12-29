class Map:
    def __init__(self):
        # width = 15
        # height = 15
        # level structure (walls, paths, enemies...)
        # sprites

        ### Don't forget to implement a refresh everytime an event occurs, maps stays in BG
        ### Can't walk on walls, can't go out of the grid
    def __hash__(self):
        return hash(self.position)
        pass
    ### Storing positions in a dictionary ?
    pass