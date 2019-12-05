import csv
import json
import os
import math
import sys


def array_print(input_array):
    for row in input_array:
        print(row)

rows, cols = (12, 12)
wire_map = [['o']*cols]*rows

def place_wire(map, instructions):

    current_column = 0
    current_row = len(map) - 1

    for i in instructions:
        direction = i[:1]

        if direction == 'R':
            number = int(i[1:])
            for x in range(0, number):
                print(number)
                map[current_row][current_column+x] = '1'

            current_column += int(i[1:])
        elif direction == 'L':
            current_column -= int(i[1:])
        elif direction == 'D':
            current_row += int(i[1:])
        elif direction == 'U':
            current_row -= int(i[1:])

    return map


array_print(wire_map)



filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

    wire_1 = next(input_reader)
    wire_2 = next(input_reader)

    wire_map = place_wire(wire_map, wire_1)
    array_print(wire_map)
