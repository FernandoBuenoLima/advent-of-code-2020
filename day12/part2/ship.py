NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'

MOVE_WAYPOINT_ACTIONS = (NORTH, SOUTH, EAST, WEST)
TURN_WAYPOINT_ACTIONS = (LEFT, RIGHT)

DIRECTIONS = { NORTH:[0,-1], SOUTH:[0,1], EAST:[1,0], WEST:[-1,0] }

class Ship:
    def __init__(self):
        self.position = [0,0]
        self.waypoint = [10,-1]

    def manhattan_distance(self):
        p = self.position
        return abs(p[0]) + abs(p[1])

    def move_waypoint(self, direction, value):
        d = DIRECTIONS[direction]
        m = [d[0]*value, d[1]*value]
        self.waypoint[0] += m[0]
        self.waypoint[1] += m[1]

    def turn_waypoint(self, direction, value):
        times = int(value/90)
        for i in range(times):
            if direction == LEFT:
                self.turn_left()
            else:
                self.turn_right()

    def turn_left(self):
        x = self.waypoint[1]
        y = -self.waypoint[0]
        self.waypoint = [x,y]

    def turn_right(self):
        x = -self.waypoint[1]
        y = self.waypoint[0]
        self.waypoint = [x,y]

    def move_ship(self, value):
        w = self.waypoint
        self.position[0] += w[0]*value
        self.position[1] += w[1]*value

    def follow_command(self, action, value):
        if action in MOVE_WAYPOINT_ACTIONS:
            self.move_waypoint(action, value)
        elif action in TURN_WAYPOINT_ACTIONS:
            self.turn_waypoint(action, value)
        else:
            self.move_ship(value)
