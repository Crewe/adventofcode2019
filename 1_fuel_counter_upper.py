import aoc
import math

def calculateTotalFuelRequirement(mass):
    fuel = math.floor(int(mass) / 3.0) - 2.0
    if (fuel <= 0):
        return 0
    return fuel + calculateTotalFuelRequirement(fuel)

def calculateFuel(filename):
    result = 0
    masses = aoc.getInput(filename)
    for mass in masses:
        # Part 1 ---
        #equiv = math.floor(int(mass) / 3.0) - 2.0 
        # --------
        equiv = calculateTotalFuelRequirement(mass)
        result = result + int(equiv)
    return result

filename = "input1.txt"
print(calculateFuel(filename))
