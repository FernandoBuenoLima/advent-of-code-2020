from map import Map

m = Map(open("input.txt").readlines())

slope = [3, 1]
trees = 0

while True:
    pos = m.move(slope)
    if pos == '.':
        continue
    elif pos == '#':
        trees += 1
    elif pos == 'e':
        break
    else:
        print("wtf is this on the map?", pos)
        exit()
        
print(trees)
exit()
