#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below
class Player:
    """a data type for Connect Four players
    """
    def __init__(self, checker):
        """a constructor for Player objects that initializes two attributes
            input: checker is either X or O
        """
        assert(checker == 'X' or checker == 'O')
        self.num_moves = 0
        self.checker = checker
    def __repr__(self):
        """returns a string representing a Player object
        """
        return 'Player ' + self.checker
    def opponent_checker(self):
        """returns a one-character string representing the checker of
            the Player object's opponent
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    def next_move(self, board):
        """returns the column where the player wants to make the next move.
            input: board is a Board object.
        """
        self.num_moves += 1
        width = board.width
        while True:
            col = int(input('Enter a column: '))
            if 0 <= col < width:
                return col
            print('Try again!')
        
        
                   
    

    
