from conway import Conway

inputs = [line.strip() for line in open("input.txt").readlines()]

c = Conway()
c.set_initial_state(inputs)

for i in range(6):
    c.cycle()

print(len(c.cubes))
exit()
