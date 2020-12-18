#R.I.P John

class Conway:
    def __init__(self):
        self.cubes = set()
    
    def set_initial_state(self, initial_state):
        is_len = len(initial_state)
        for x in range(is_len):
            for y in range(is_len):
                if initial_state[x][y] == '#':
                    self.set_cube_on((x, y, 0, 0))
    
    def get_cube(self, cube):
        return cube in self.cubes
    
    def set_cube_on(self, cube):
        self.cubes.add(cube)
    
    def set_cube_off(self, cube):
        if cube in self.cubes:
            self.cubes.remove(cube)
    
    def cycle(self):
        d = self.get_neighbors_dict()
        to_remove = set()
        to_add = set()
        for cube in d:
            n = d[cube]
            if self.get_cube(cube):
                if n != 2 and n != 3:
                    to_remove.add(cube)
            else:
                if n == 3:
                    to_add.add(cube)
        
        for cube in to_remove:
            self.set_cube_off(cube)
        for cube in to_add:
            self.set_cube_on(cube)
    
    def get_neighbors_dict(self):
        n = dict()        
        for cube in self.cubes:
            for x in range(cube[0]-1, cube[0]+2):
                for y in range(cube[1]-1, cube[1]+2):
                    for z in range(cube[2]-1, cube[2]+2):
                        for w in range(cube[3]-1, cube[3]+2):
                            c = (x, y, z, w)
                            if c == cube:
                                if c not in n:
                                    n[c] = 0
                                continue
                            if c in n:
                                n[c] += 1
                            else:
                                n[c] = 1
        return n