import aoc

wire_paths = aoc.getInput("input3.txt")
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

def findLineSegments(wire):
    seg = [[0,0,0,0]]
    index = 0
    for direction in wire:
        heading = direction[0]
        dist = int(direction[1:])
        prev_point = (seg[index][0], seg[index][1])  #x0,y0
        next_point = ()
        if heading == 'L' or heading == 'D': dist *= -1
        if heading == 'L' or heading == 'R':
            next_point = (prev_point[0] + dist, prev_point[1])
        elif heading == 'U' or heading == 'D':
            next_point = (prev_point[0], prev_point[1] + dist)
        seg[index][2] = next_point[0] #x1
        seg[index][3] = next_point[1]  #y1
        seg[index] = tuple(seg[index])
        seg.append([next_point[0], next_point[1], 0, 0])
        index += 1
    seg.remove(seg[-1]) # remove point
    return seg

def findIntersections(wire_1, wire_2):
    # Find horizontal wire_1 segments that cross wire_2 vertically

    # Find vertical wire_1 segments that cross wire_2 horizontally

for line in findLineSegments(wire_1):
    print(line)
for line in findLineSegments(wire_2):
    print(line)
