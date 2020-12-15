class Bus:
    def __init__(self, id, shift):
        self.id = id
        self.shift = shift
        
    def __str__(self):
        return "id: " + str(self.id) + " shift: " + str(self.shift)
    
    def check(self, base):
        return (base + self.shift) % self.id == 0