import csv
import json
import os
import math
import sys

from intcode import IntCode

def main():
    computer = IntCode(sys.argv[1])

    print(computer.memory_size)
    for i in range(computer.memory_size):
        for j in range(computer.memory_size):
            computer.re_init()
            computer.run(i, j)

            output = computer.output

            # print(output)

            if output == 19690720:
                print(i, j)
                print('ya did it')
                break

main()
