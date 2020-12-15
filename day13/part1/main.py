from math import ceil

def get_departure(bus, my_time):
    mult = ceil(my_time / bus)
    return bus * mult

with open("input.txt") as file:
    my_time = int(file.readline().strip())
    inputs = [bus.strip() for bus in file.readline().split(',')]

busses = [int(bus) for bus in inputs if bus != 'x']
departures = [get_departure(bus, my_time) for bus in busses]

departure = min(departures)
wait_time = departure - my_time
bus = busses[departures.index(departure)]

print(bus * wait_time)
exit()