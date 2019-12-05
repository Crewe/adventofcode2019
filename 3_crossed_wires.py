import aoc

wire_paths = aoc.getInput("test.txt")
wire_1 = aoc.csvToList(wire_paths[0])
wire_2 = aoc.csvToList(wire_paths[1])

def findMaximums(wire):
    maximums = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
    for direction in wire:
        heading = direction[0]
        dist = int(direction[1:])
        if heading == 'L' or heading == 'D':
            dist *= -1
        maximums[heading] += dist
    return maximums

MAX = 40000
print(findMaximums(wire_1))
print(findMaximums(wire_2))