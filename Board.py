#
#A Connect Four Board Class

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """
    def __init__(self, height, width):
        """ a constructor for Board objects that specifies three attributes
            inputs: height and width are integers
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for r in range(self.height)]
    def __repr__(self):
        """ returns a string representing a Board object
        """
        s = ''
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'
        len_l = self.width * 2 + 1
        s += '-' * len_l
        s += '\n'
        for c in range(self.width):
            s += ' '
            s += str(c % 10)
        return s
    def add_checker(self, checker, col):
        """ adds the specified checker to a specified column on a Board
            object.
            input: checker is either X or O, column is an integer
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        row = 0
        for r in range(self.height):
            if self.slots[row][col] == ' ':
                row += 1
        self.slots[row - 1][col] = checker
    def reset(self):
        """reset the Board object by setting all slots to containing
            a space character.
        """
        self.slots = [[' '] * self.width for r in range(self.height)]
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
    def can_add_to(self, col):
        """returns True is it is valid to place a checker in the column,
            returns False if col is out of range, or the specified column
            is full.
            input: col is an integer
        """
        if col < 0 or col > self.width - 1:
            return False
        elif self.slots[0][col] != ' ':
            return False
        else:
            return True
    def is_full(self):
        """returns True if the called Board object is completely full of
            checkers, and returns False otherwise.
        """
        for c in range(self.width):
            if self.can_add_to(c) == True:
                return False
        return True
    def remove_checker(self, col):
        """removes the top checker from column col, does nothing if the
            specified column is empty
            input: col is an integer
        """
        row = 0
        for r in range(self.height):
            if self.slots[r][col] == ' ':
                row += 1
        if row < self.height:
            self.slots[row][col] = ' '
    def is_horizontal_win(self, checker):
        """checks for a horizontal win for the specified checker
        """
        for row  in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False
    def is_vertical_win(self, checker):
        """checks for a vertical win for the specified checker
        """
        for col in range(self.width):
            for row in range(self.height - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False
    def is_down_diagonal_win(self, checker):
        """checks for a down diagonal win for the specified checker
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        return False
    def is_up_diagonal_win(self, checker):
        """checks for a up diagonal win for the specified checker
        """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
        return False
    def is_win_for(self, checker):
        """returns True if there are four consecutive slots containing
            the specified checker, and returns False if otherwise.
            input: checker is either 'X' or 'O'
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False
        
            
        
        
        
        

            
        
            
    
            
