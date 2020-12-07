from bag import Bag

bags = [Bag(line) for line in open("input.txt").readlines()]

def get_bag_of_type(type):
    for bag in bags:
        if bag.type == type:
            return bag
    return None

def can_bag_contain_type(bag, type):
    if bag.can_directly_contain_type(type):
        return True
    
    for c in bag.contained:
        contained_bag = get_bag_of_type(c["type"])
        if can_bag_contain_type(contained_bag, type):
            return True
    
    return False

total = 0

for bag in bags:
    if can_bag_contain_type(bag, "shiny gold"):
        total += 1
    
print(total)

exit()
