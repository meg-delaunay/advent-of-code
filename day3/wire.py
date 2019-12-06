
class Wire:
    def __init__(self, instructions):
        self.placed_coordinates = []
        current_row = 0
        current_col = 0
        for instruct in instructions:

            direction = instruct[:1]
            number = int(instruct[1:])

            if direction == 'R':
                for x in range(0, number):
                    self.placed_coordinates.append((current_row, current_col))
                    current_col += 1
            elif direction == 'L':
                for x in range(0, number):
                    self.placed_coordinates.append((current_row, current_col))
                    current_col -= 1
            elif direction == 'U':
                for x in range(0, number):
                    self.placed_coordinates.append((current_row, current_col))
                    current_row += 1
            elif direction == 'D':
                for x in range(0, number):
                    self.placed_coordinates.append((current_row, current_col))
                    current_row -= 1
