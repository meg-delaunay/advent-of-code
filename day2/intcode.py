import csv
import json
import os
import math
import sys

class IntCode:
    def __init__(self, filename):
        self.memory = []

        with open(filename) as input_file:
            input_reader = csv.reader(input_file, delimiter=',', quotechar='|')

            for row in input_reader:
                self.memory = row
            self.memory = [int(number) for number in self.memory]
            self.init_memory = self.memory.copy()

            self.memory_size = len(self.memory)

    def re_init(self):
        self.memory = self.init_memory.copy()

    def run(self, noun, verb):
        # cprint(self.memory)
        instruction_pointer = 0
        while(instruction_pointer < len(self.memory)):
            opcode = self.memory[instruction_pointer]

            if opcode == 99:
                break

            if instruction_pointer == 0:
                self.memory[instruction_pointer+1] = noun
                self.memory[instruction_pointer+2] = verb

            # gets the values of the three parameters
            output_address_1 = int(self.memory[instruction_pointer+3])
            input_address_1 = int(self.memory[instruction_pointer+1])
            input_address_2 = int(self.memory[instruction_pointer+2])

            # gets the values at the addresses marked in the parameters
            input_value_1 = int(self.memory[input_address_1])
            input_value_2 = int(self.memory[input_address_2])

            if opcode == 1:
                output_value = input_value_1 + input_value_2
                self.memory[output_address_1] = output_value
            elif opcode == 2:
                output_value = input_value_1 * input_value_2
                self.memory[output_address_1] = output_value
            else:
                print("megan sucks")

            instruction_pointer += 4
        self.output = self.memory[0]
