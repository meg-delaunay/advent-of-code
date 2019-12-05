import csv
import json
import os
import math
import sys

global COL_SIZE
global ROW_SIZE

from wiremap import WireMap

# COL_SIZE = 4
# ROW_SIZE = 2
#
# def array_print(input_array):
#     for row in input_array:
#         print(row)
#
# wire_map = [['o'] * COL_SIZE for i in range(ROW_SIZE)]


# def extend_map_left(map):
#     for row in map:
#         row.insert(0, 'o')
#
#     COL_SIZE += 1
#     return map
#
# def extend_map_right(map):
#     for row in map:
#         row.append('o')
#
#     COL_SIZE += 1
#     return map
#
# def extend_map_up(map):
#     new_array = ['o'] * COL_SIZE
#     map.insert(0, new_array)
#
#     ROW_SIZE += 1
#     return map
#
# def extend_map_down(map):
#     new_array = ['o'] * COL_SIZE
#     map.append(new_array)
#
#     ROW_SIZE += 1
#     return map
#
# def place_wire(map, instructions, token):
#     current_column = 0
#     current_row = len(map) - 1
#
#     print(type(instructions))
#     print(len(instructions))
#     print(instructions[0])
#
#     for i in instructions:
#         print(i)
#         direction = i[:1]
#
#         if direction == 'R':
#             number = int(i[1:])
#             for x in range(0, number):
#                 if x >= len(map[current_row]):
#                     print('hello')
#                     map = extend_map_right(map)
#                 map[current_row][current_column+x] = token
#
#             current_column += int(i[1:])
#         elif direction == 'L':
#             number = int(i[1:])
#             for x in range(0, number):
#                 if current_column-x < 0:
#                     map = extend_map_left(map)
#                     current_column = current_column + 1
#                 map[current_row][current_column-x] = token
#
#             current_column -= int(i[1:])
#         elif direction == 'D':
#             # current_row += int(i[1:])
#
#             number = int(i[1:])
#             for x in range(0, number):
#                 print('x', x)
#                 print('row', current_row+x)
#                 # array_print(map)
#                 if current_row+x >= len(map):
#                     print('extendinng')
#                     map = extend_map_down(map)
#                     #array_print(map)
#                 map[current_row+x][current_column] = token
#
#             current_row += 1
#         elif direction == 'U':
#             number = int(i[1:])
#             for x in range(0, number):
#                 print('x', x)
#                 print('row', current_row-x)
#                 #array_print(map)
#                 if current_row-x < 0:
#                     map = extend_map_up(map)
#                     current_row += 1
#                 map[current_row-x][current_column] = token
#
#             current_row += 1
#
#     return map


map = WireMap(sys.argv[1])
map.place_wire(map.wire_1, '1')
map.place_wire(map.wire_2, '2')

map.wire_print()
