from console import Console

input = [line.strip() for line in open("input.txt").readlines()]

console = Console(input)
print(console.execute_until_repeat())

exit()