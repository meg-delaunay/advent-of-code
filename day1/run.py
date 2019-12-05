import csv
import json
import os
import math
import sys

def calculate_fuel(mass):
    if mass <= 0:
        return 0

    next_val = math.floor((mass/3)) - 2
    return mass + calculate_fuel(next_val)

filename = sys.argv[1]
with open(filename) as input_file:
    input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

    total_fuel = 0
    for row in input_reader:

        mass = int(row[0])
        original_fuel = math.floor((mass/3)) - 2


        total_module_fuel = calculate_fuel(original_fuel)
        total_fuel += total_module_fuel

print(total_fuel)
