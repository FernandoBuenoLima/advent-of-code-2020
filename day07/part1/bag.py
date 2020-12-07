def get_color_from_string(s):
    if s.endswith("bag"):
        return s[:-4]
    return s[:-5]

class Bag:
    def __init__(self, data):
        container_str, contained_str = data.split("contain")
        
        self.type = get_color_from_string(container_str.strip())
        self.contained = list()
        
        contained_str = contained_str.strip()[:-1]
        if contained_str != "no other bags":
            contained_list = [c.strip() for c in contained_str.split(',')]
            for c in contained_list:
                self.contained.append( { "amount":int(c[0]), "type":get_color_from_string(c[2:]) })
    
    def __str__(self):
        return str(self.type) + '\n' + str(self.contained)

    def can_directly_contain_type(self, type):
        for t in self.contained:
            if t["type"] == type:
                return True
        return False
