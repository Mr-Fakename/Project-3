class Position:
    """ This class handles positions and movement methods
        Used as parent class for every class
    """
    def __init__(self, x, y):
        self.position = (x, y)

    def __repr__(self):
        # Makes it possible to have a visualization of the position as tuple and not object in memory
        return str(self.position)

    def __hash__(self):
        # Used with __eq__ to compare positions
        return hash(self.position)

    def __eq__(self, pos):
        # Set the behavior of the comparison between positions, mainly for collisions
        return self.position == pos.position

    def move_up(self):
        x, y = self.position
        return x - 1, y

    def move_right(self):
        x, y = self.position
        return x, y + 1

    def move_left(self):
        x, y = self.position
        return x, y - 1

    def move_down(self):
        x, y = self.position
        return x + 1, y

    def valid_move(self, direction):
        """ The "valid_move" function is used to compute where the moving things are allowed to go
                                        by verifying the existence an element in the "walls" set()
            "getattr" gets an argument from a string and keeps the code DRY
        """
        new_position = getattr(self, direction)()
        if new_position not in self.map.walls:
            # Could use "if in map.paths" instead, avoids character going out of the map for now
            self.position = new_position
