from ticket import Validator

inputs = [s for s in open("input.txt").read().split("\n\n")]

validator = Validator(inputs[0])

nearby_tickets = []

for line in inputs[2].split('\n'):
    if line.startswith("nearby tickets:"):
        continue
    nearby_tickets.append([int(v.strip()) for v in line.split(',')])
    
valid_tickets = [ticket for ticket in nearby_tickets if validator.validate_ticket(ticket)]

possible_fields = []
for value in valid_tickets[0]:
    possible_fields.append(validator.get_valid_fields_for_value(value))
del valid_tickets[0]

for ticket in valid_tickets:
    for i in range(len(possible_fields)):
        possible_fields[i] = validator.get_valid_fields_for_value(ticket[i], possible_fields[i])

certain_fields = set()

while len(certain_fields) < len(possible_fields):
    for i in range(len(possible_fields)):
        if i not in certain_fields:
            possible = possible_fields[i]
            if len(possible) == 1:
                for key in possible:
                    f = key
                certain_fields.add(i)
                for j in range(len(possible_fields)):
                    if j not in certain_fields:
                        if f in possible_fields[j]:
                            possible_fields[j].remove(f)

my_ticket = [int(v.strip()) for v in inputs[1].split('\n')[1].split(',')]

total = 1

for i in range(len(possible_fields)):
    for key in possible_fields[i]:
        if key.startswith("departure"):
            total *= my_ticket[i]

print(total)
