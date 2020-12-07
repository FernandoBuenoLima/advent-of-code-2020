from bag import Bag

bags_list = [Bag(line) for line in open("input.txt").readlines()]
bags = dict()

for bag in bags_list:
    bags[bag.type] = bag

shiny_gold = bags["shiny gold"]
print(shiny_gold.get_bags_contained(bags))

exit()
