OCCUPIED = '#'
EMPTY = 'L'
FLOOR = '.'

class Ferry:
    def __init__(self, data):
        self.layout = []
        for line in data:
            self.layout.append(line.copy())
        self.height = len(self.layout)
        self.width = len(self.layout[0])

    def __str__(self):
        s = ""
        for row in self.layout:
            s += "\n"
            for c in row:
                s += c
        return s[1:]

    def get_position(self, position):
        x = position[0]
        y = position[1]
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return None
        return self.layout[y][x]

    def set_position(self, position, value):
        x = position[0]
        y = position[1]
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            print("Trying to set to inexistent position:", position)
            print("Value:", value)
            print("For map with a size:", [self.width, self.height])
            exit()
        self.layout[y][x] = value

    def look_at(self, position, direction):
        p = position
        while True:
            p[0] += direction[0]
            p[1] += direction[1]
            current = self.get_position(p)
            if current != FLOOR:
                break
        return current


    def count_visible_occupied_seats(self, position):
        total = 0

        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == y == 0:
                    continue
                if self.look_at(position.copy(), [x, y]) == OCCUPIED:
                    total += 1
        return total

    def execute_round(self):
        new_ferry = Ferry(self.layout)
        changed = False
        for x in range(self.width):
            for y in range(self.height):
                p = [x,y]
                current = self.get_position(p)
                adj_occupied = self.count_visible_occupied_seats(p.copy())
                if current == EMPTY and adj_occupied == 0:
                    new_ferry.set_position(p, OCCUPIED)
                    changed = True
                elif current == OCCUPIED and adj_occupied >= 5:
                    new_ferry.set_position(p, EMPTY)
                    changed = True

        self.layout = new_ferry.layout
        return not changed

    def count_all_occupied_seats(self):
        total = 0
        for line in self.layout:
            for c in line:
                if c == OCCUPIED:
                    total += 1
        return total