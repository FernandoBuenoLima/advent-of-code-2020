from passport import Passport

input = open("input.txt").read().split("\n\n")

passports = [Passport(data) for data in input]

validPassports = 0

for p in passports:
    if p.isValid():
        validPassports += 1
    
print(validPassports)
