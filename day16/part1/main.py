from ticket import Validator

inputs = [s for s in open("input.txt").read().split("\n\n")]

validator = Validator(inputs[0])

error_rate = 0

for ticket in inputs[2].split('\n'):
    if ticket.startswith("nearby tickets:"):
        continue
    
    for value in ticket.split(','):
        v = int(value.strip())
        if not validator.validate_value(v):
            error_rate += v

print(error_rate)
    