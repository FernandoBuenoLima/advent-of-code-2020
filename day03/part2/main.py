from map import Map

def number_of_trees_for_slope(map, slope):
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
            print(type(pos))
            print(m.position)
            print(m.width, m.height)
            exit()
    
    return trees

m = Map(open("input.txt").readlines())

slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
answer = 1
        
for slope in slopes:
    answer *= number_of_trees_for_slope(m, slope)
    m.refresh()
        
print(answer)
exit()
