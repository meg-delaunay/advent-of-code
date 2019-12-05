import csv
import json
import os
import math
import sys

class WireMap:
    def __init__(self, filename):
        self.COL_SIZE = 2
        self.ROW_SIZE = 2

        self.map = [['o'] * self.COL_SIZE for i in range(self.ROW_SIZE)]

        with open(filename) as input_file:
            input_reader = csv.reader(input_file, delimiter='\n', quotechar='|')

            rows = []
            for row in input_reader:
                rows.append(row[0])

            self.wire_1 = rows[0].split(',')
            self.wire_2 =rows[1].split(',')

        self.starting_point = {'row':len(self.map) - 1, 'col':0}
        print(self.starting_point)

    def wire_print(self):
        for row in self.map:
            print(row)

    def extend_map_left(self):
        for row in self.map:
            row.insert(0, 'o')

        self.starting_point['col'] = self.starting_point.get('col') + 1
        self.COL_SIZE += 1

    def extend_map_right(self):
        for row in self.map:
            row.append('o')

        self.COL_SIZE += 1

    def extend_map_up(self):
        new_array = ['o'] * self.COL_SIZE
        self.map.insert(0, new_array)

        self.starting_point['row'] = self.starting_point.get('row') + 1
        self.ROW_SIZE += 1

    def extend_map_down(self):
        new_array = ['o'] * self.COL_SIZE
        self.map.append(new_array)

        self.ROW_SIZE += 1

    def place_token(self, token, row, col):
        print(row, col)
        if self.map[row][col] == 'o':
            self.map[row][col] = token
        elif (self.map[row][col] == token) or (self.map[row][col] == 'S'):
            pass
        else:
            self.map[row][col] = 'B'

    def place_wire(self, instructions, token):
        # need to keep track of starting point and re-init to those places here

        current_column = int(self.starting_point.get('col'))
        current_row = int(self.starting_point.get('row'))

        self.map[current_row][current_column] = 'S'

        for i in instructions:
            self.wire_print()
            print(i)
            direction = i[:1]

            if direction == 'R':
                number = int(i[1:])
                for x in range(0, number):
                    print(x)
                    if current_column+x >= len(self.map[current_row]):
                        print('hello')
                        self.extend_map_right()
                    self.place_token(token, current_row, current_column+x)
                    # self.map[current_row][current_column+x] = token

                current_column += int(i[1:]) - 1
            elif direction == 'L':
                number = int(i[1:])
                for x in range(0, number):
                    if current_column-x < 0:
                        self.extend_map_left()
                        current_column = current_column + 1
                    self.place_token(token, current_row, current_column-x)
                    # self.map[current_row][current_column-x] = token

                current_column -= number-1
            elif direction == 'D':
                # current_row += int(i[1:])

                number = int(i[1:])
                for x in range(0, number):
                    print('x', x)
                    print('row', current_row+x)
                    print('col', current_column)
                    # array_print(map)
                    if current_row+x >= len(self.map):
                        print('extendinng')
                        self.extend_map_down()
                        #array_print(map)
                    self.place_token(token, current_row+x, current_column)
                    # self.map[current_row+x][current_column] = token

                current_row += int(i[1:]) -1
            elif direction == 'U':
                print('col on up', current_column)
                number = int(i[1:])
                for x in range(0, number):
                    print('x', x)
                    print('row', current_row-x)
                    #array_print(map)
                    if current_row-x < 0:
                        self.extend_map_up()
                        current_row += 1
                    self.place_token(token, current_row-x, current_column)
                    # self.map[current_row-x][current_column] = token

                current_row -= int(i[1:])-1
