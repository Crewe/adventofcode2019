import aoc
import math

wire_paths = aoc.getInput("input3.txt")
wire_1 = aoc.csvToList(wire_paths[0])
wire_2 = aoc.csvToList(wire_paths[1])

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

def findIntersections(wire_1_segs, wire_2_segs):
    ''' 
    This will find the horizontal segments from the first list, and compare it
    to the vertical segments of the second list. Then swap the lists and do the
    same comparison it find all intersections.
    '''
    poi = []
    bit = 0 # To flip lists instead of running the function twice
    segment_list = [wire_1_segs, wire_2_segs]
    while bit < 2:
        for h_line in segment_list[0 + bit]:
            # Find horizontal segments
            if h_line[1] == h_line[3]:
                y = h_line[1]
                x0 = h_line[0]
                x1 = h_line[2]
                for v_line in segment_list[1 - bit]:
                    # Find vertical segments
                    if v_line[0] == v_line[2]:
                        x = v_line[0]
                        y0 = v_line[1]
                        y1 = v_line[3]
                        # Check if the segments cross
                        if ((x0 < x < x1) or (x1 < x < x0)) and ((y0 < y < y1) or (y1 < y < y0)):
                            poi.append((x,y))
        bit+=1
    return poi

def findShortestManhattanDistance(point_list):
    magnitude = 0
    for point in point_list:
        # Finding the shortest magnitude irrelevant of direction
        manhattan_dist = abs(point[0]) + abs(point[1])
        if magnitude == 0:
            magnitude = manhattan_dist
        elif (manhattan_dist <= magnitude):
            magnitude = manhattan_dist
    return magnitude

intersections = findIntersections(findLineSegments(wire_1), findLineSegments(wire_2))
distance = findShortestManhattanDistance(intersections)
print(distance)