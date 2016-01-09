#Name: Teng Xu
#E-mail: xt@bu.edu

class Board:
    def __init__(self):
         """ a constructor for Board objects """
         self.slots = [['  '] * 8 for row in range(8)]
         self.slots[0][0] = 'rd'
         self.slots[0][1] = 'nd'
         self.slots[0][2] = 'bd'
         self.slots[0][3] = 'qd'
         self.slots[0][4] = 'kd'
         self.slots[0][5] = 'bd'
         self.slots[0][6] = 'nd'
         self.slots[0][7] = 'rd'
         self.slots[1][0] = 'pd'
         self.slots[1][1] = 'pd'
         self.slots[1][2] = 'pd'
         self.slots[1][3] = 'pd'
         self.slots[1][4] = 'pd'
         self.slots[1][5] = 'pd'
         self.slots[1][6] = 'pd'
         self.slots[1][7] = 'pd'
         self.slots[7][0] = 'rl'
         self.slots[7][1] = 'nl'
         self.slots[7][2] = 'bl'
         self.slots[7][3] = 'ql'
         self.slots[7][4] = 'kl'
         self.slots[7][5] = 'bl'
         self.slots[7][6] = 'nl'
         self.slots[7][7] = 'rl'
         self.slots[6][0] = 'pl'
         self.slots[6][1] = 'pl'
         self.slots[6][2] = 'pl'
         self.slots[6][3] = 'pl'
         self.slots[6][4] = 'pl'
         self.slots[6][5] = 'pl'
         self.slots[6][6] = 'pl'
         self.slots[6][7] = 'pl'

      
    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string
        # add one row of slots at a time
        for n in range(8):
            s += '  '
            s += str(n)
        s += '\n'
        for row in range(8):
            s += str(row)
            s += '|'   # one vertical bar at the start of the row
            for col in range(8):
                s += self.slots[row][col] + '|'
            s += '\n'  # newline at the end of the row
        return s


class Board2:
    def __init__(self):
        self.slots = [['x'] * 8 for row in range(8)]

    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ' '         # begin with an empty string
        # add one row of slots at a time
        for n in range(8):
            s += ' '
            s += str(n)
        s += '\n'
        for row in range(8):
            s += str(row)
            s += '|'   # one vertical bar at the start of the row
            for col in range(8):
                s += self.slots[row][col] + '|'
            s += '\n'  # newline at the end of the row
        return s

    def clear(self):
        self.slots = [['x'] * 8 for row in range(8)]
