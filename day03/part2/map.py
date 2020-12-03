class Map:
    def __init__(self, data):
        self.data = [line.strip() for line in data]
        self.position = [0, 0]
        self.height = len(self.data)
        self.width = len(self.data[0])
    
    def refresh(self):
        self.position = [0, 0]
    
    def getPosition(self):
        if self.position[1] >= self.height:
            return 'e'
        return self.data[self.position[1]][self.position[0]]
    
    def move(self, delta):
        self.position[0] += delta[0]
        while self.position[0] >= self.width:
            self.position[0] -= self.width
        self.position[1] += delta[1]
        return self.getPosition()