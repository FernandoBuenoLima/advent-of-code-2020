NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'

MOVE_ACTIONS = (NORTH, SOUTH, EAST, WEST, FORWARD)

DIRECTIONS = { NORTH:[0,-1], SOUTH:[0,1], EAST:[1,0], WEST:[-1,0] }

R_S = [NORTH, EAST, SOUTH, WEST, NORTH, EAST, SOUTH]
L_S = R_S.copy()
L_S.reverse()
DIRECTIONS_SEQUENCES = { RIGHT:R_S, LEFT:L_S}


class Ship:
    def __init__(self):
        self.facing = EAST
        self.position = [0,0]

    def manhattan_distance(self):
        p = self.position
        return abs(p[0]) + abs(p[1])

    def move(self, direction, value):
        if direction == FORWARD:
            direction = self.facing
        d = DIRECTIONS[direction]
        m = [d[0]*value, d[1]*value]
        self.position[0] += m[0]
        self.position[1] += m[1]

    def turn(self, direction, value):
        sequence = DIRECTIONS_SEQUENCES[direction]
        i = sequence.index(self.facing)
        i += int(value/90)
        self.facing = sequence[i]

    def follow_command(self, action, value):
        if action in MOVE_ACTIONS:
            self.move(action, value)
        else:
            self.turn(action, value)
