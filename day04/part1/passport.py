
requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

class Passport:
    def __init__(self, data):
        self.fields = dict()
        fieldPairs = [a.strip() for a in data.split()]
        for pair in fieldPairs:
            key, value = pair.split(':')
            self.fields[key] = value
    
    def hasField(self, key):
        return key in self.fields
    
    def isValid(self):
        for required in requiredFields:
            if not self.hasField(required):
                return False
        return True
    