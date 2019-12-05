import aoc

EOF = 0
filename = "input2.txt"

def add(program, a, b, r):
    program[r] = a + b

def product(program, a, b, r):
    program[r] = a * b

def runProgram(program):
    pos = 0
    for i in range(EOF):
        program[i] = int(program[i])

    while program[pos] != 99:
        op = program[pos]
        r_a = program[pos + 1]
        r_b = program[pos + 2]
        r_r = pos + 3
        
        if op == 1: add(program, program[r_a], program[r_b], program[r_r])
        elif op == 2: product(program, program[r_a], program[r_b], program[r_r])
        pos += 4
        if pos > EOF: exit
    return program

def PartOne(program_state):
    program_state = aoc.getInput(filename, 'csv')
    EOF = len(program_state)
    # Set Pre-alarm state
    program_state[1] = '12' #noun
    program_state[2] = '2'  #verb
    result = runProgram(program_state)
    print("Part 1: {}".format(result[0]))

def PartTwo():
    for noun in range(99, 0, -1):
        for verb in range(100):
            intcode = aoc.getInput(filename, 'csv')
            intcode[1] = noun
            intcode[2] = verb
            result = runProgram(intcode)
            if result[0] == 19690720:
                print("Part 2: noun: {}, verb: {}".format(noun, verb))
                print("        100 * noun + verb = {}".format(100 * noun + verb))
                return
    print("Part 2: Result not found.")

program_state = aoc.getInput(filename, 'csv')
EOF = len(program_state)
PartOne(program_state)
PartTwo()