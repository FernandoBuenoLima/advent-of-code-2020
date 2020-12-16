class Validator:
    def __init__(self, rules_str):
        self.rules = {}
        for rule_str in rules_str.split('\n'):
            name, ranges = rule_str.split(':')
            ranges_list = []
            for range in ranges.split("or"):
                min, max = range.split('-')
                ranges_list.append([int(min.strip()), int(max.strip())])
            self.rules[name] = ranges_list
    
    def validate_ticket(self, ticket):
        for value in ticket:
            if not self.validate_value(value):
                return False
        return True
                
    def validate_value(self, value):
        for name in self.rules:
            if self.validate_value_for_ranges(value, self.rules[name]):
                return True
        return False
    
    def validate_value_for_ranges(self, value, ranges):
        for range in ranges:
            if value >= range[0] and value <= range[1]:
                return True
        return False
    
    def get_valid_fields_for_value(self, value, field_names = None):
        ret = set()
        if field_names is None:
            field_names = self.rules
        for name in field_names:
            if self.validate_value_for_ranges(value, self.rules[name]):
                ret.add(name)
        return ret