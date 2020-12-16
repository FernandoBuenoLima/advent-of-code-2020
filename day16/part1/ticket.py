class Validator:
    def __init__(self, rules_str):
        self.rules = []
        for rule_str in rules_str.split('\n'):
            rule = rule_str.split(':')[1]
            for range in rule.split("or"):
                min, max = range.split('-')
                self.rules.append([int(min.strip()), int(max.strip())])
                
    def validate_value(self, value):
        for rule in self.rules:
            if value >= rule[0] and value <= rule[1]:
                return True
        return False