import io
import os
import csv

def getInput(filename, type=''):
    working_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(working_dir, filename)
    value_array = []
    with open(file) as f:
        if type == 'csv':
            reader = csv.reader(f)
            return list(reader)[0]
        else:
            for line in f:
                value_array.append(line.replace('\n', ''))
            return value_array