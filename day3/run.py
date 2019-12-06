import csv
import json
import os
import math
import sys

from wire import Wire


def find_connections(wire1, wire2):
    matches = []

    for point in wire1.placed_coordinates:
        for point2 in wire2.placed_coordinates:
            if point == point2 and point != (0,0):
                matches.append(point)

    return matches

def calculate_distance(point):
    x_dis = abs(point[0])
    y_dis = abs(point[1])

    return x_dis+y_dis

with open(sys.argv[1]) as input_file:
    input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

    rows = []
    for row in input_reader:
        rows.append(row[0])

    wire_1_instructions = rows[0].split(',')
    wire_2_instructions =rows[1].split(',')

    wire1 = Wire(wire_1_instructions)
    wire2 = Wire(wire_2_instructions)

    connections = find_connections(wire1, wire2)

    distance = 1000000000000000
    for c in connections:
        new_dis = calculate_distance(c)
        if new_dis < distance:
            distance = new_dis

    print('final answer!', distance)
