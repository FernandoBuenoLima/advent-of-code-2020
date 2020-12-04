
requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
hex_chars = "0123456789abcdef"
eye_color_values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

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
        if not self.validate_byr():
            return False
        if not self.validate_iyr():
            return False
        if not self.validate_eyr():
            return False
        if not self.validate_hgt():
            return False
        if not self.validate_hcl():
            return False
        if not self.validate_ecl():
            return False
        if not self.validate_pid():
            return False    
        return True
    
    def validate_byr(self):
        value = self.fields['byr']
        if len(value) != 4:
            return False
        if not value.isdigit():
            return False
        return 1920 <= int(value) <= 2002
        
    def validate_iyr(self):
        value = self.fields['iyr']
        if len(value) != 4:
            return False
        if not value.isdigit():
            return False
        return 2010 <= int(value) <= 2020
        
    def validate_eyr(self):
        value = self.fields['eyr']
        if len(value) != 4:
            return False
        if not value.isdigit():
            return False
        return 2020 <= int(value) <= 2030
        
    def validate_hgt(self):
        value = self.fields['hgt']
        number = int(value[:-2])
        unit = value[-2:]
        if unit == 'cm':
            return 150 <= number <= 193
        elif unit == 'in':
            return 59 <= number <= 76
        return False
        
    def validate_hcl(self):
        value = self.fields['hcl']
        if len(value) != 7:
            return False
        if value[0] != '#':
            return False
        for c in value[1:]:
            if c not in hex_chars:
                return False
        return True
        
    def validate_ecl(self):
        value = self.fields['ecl']
        return value in eye_color_values
        
    def validate_pid(self):
        value = self.fields['pid']
        return len(value) == 9 and value.isdigit()
