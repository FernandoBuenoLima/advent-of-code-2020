from ship import *

inputs = [line.strip() for line in open("input.txt").readlines()]

ship = Ship()

for command in inputs:
    action = command[0]
    value = int(command[1:])
    ship.follow_command(action, value)

print(ship.manhattan_distance())
exit()