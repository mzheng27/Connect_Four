#
# Playing the game 
#   

from Connect_four_board import Board
from Connect_four_player import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board

#task 1
def process_move(player, board):
    """performs all of the steps involved in processing a single move by
        the specified player on teh specified board
        inputs: player is either 'X' or 'O', board is a Board object
    """
    p1 = player
    b1 = board 
    print(p1, end = '')
    print("'s turn")
    col = p1.next_move(b1)
    if b1.can_add_to(col) == True:
        b1.add_checker(p1.checker, col)
    print()
    print(b1)
    print()
    if b1.is_win_for(p1.checker) == True:
        print(p1, end = '')
        print(' wins in ' + str(p1.num_moves) \
              + ' moves.\nCongratulations!')
        return True
    elif b1.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False

#task 2
class RandomPlayer(Player):
    """a subclass of Player, a data type for an unintelligent computer player
        inherits attributes from Player, overrides the next_move method in Player
    """
    def next_move(self, board):
        """chooses at random from the columns in the specified board that
            are not yet full, return the index of that column
            input: board is not full
        """
        self.num_moves += 1
        ava_col = []
        for c in range(board.width):
            if board.can_add_to(c) == True:
                ava_col += [c]
        print(ava_col)
        col = random.choice(ava_col)
        return col
        
    
    
    
        
    
    
          
