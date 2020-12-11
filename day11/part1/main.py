from ferry import Ferry

input = [line.strip() for line in open("input.txt").readlines()]

data = []

for line in input:
    l = []
    for c in line:
        l.append(c)
    data.append(l)

ferry = Ferry(data)

while not ferry.execute_round():
    pass

print(ferry.count_all_occupied_seats())
