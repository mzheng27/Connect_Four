
#
# AI Player for use in Connect Four   
#

import random  
from CF_functions import *
class AIPlayer(Player):
    """a subclass of Player, a data type for an AI player. Inherits
        the methods of the Player class, but override some of them.
    """
    def __init__(self, checker, tiebreak, lookahead):
        """a constructor of AI player objects"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    def __repr__(self):
        """returns a string representing an AIPlayer object, override the
            __repr__ method inherited from Player
        """
        return 'Player ' + self.checker + ' (' + self.tiebreak + ', ' \
               + str(self.lookahead) + ')'
    def max_score_column(self, scores):
        """returns the index of the column with the maximum score. If
            one or more columns are tied, apply the specified tiebreaking
            strategy.
            input: scores is a list containing a score for each column of
            the board.
        """
        max_score = max(scores)
        len_scores = len(scores)
        list_index = []
        for i in range(len_scores):
            if scores[i] == max_score:
                list_index += [i]
        if self.tiebreak == 'LEFT':
            return list_index[0]
        elif self.tiebreak == 'RIGHT':
            return list_index[-1]
        else:
            return random.choice(list_index)
    def scores_for(self, board):
        """return a list containing the called AIPlayer's scores for each
            column in board.
            inputs: board is a Board object.
        """
        scores = [50] * board.width
        for col in range(board.width):
            if board.can_add_to(col) == False:
                scores[col] = -1
            elif board.is_win_for(self.checker) == True:
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                opp = AIPlayer(self.opponent_checker(), self.tiebreak, \
                               self.lookahead - 1)
                opp_scores = opp.scores_for(board)
                scores[col] = 100 - max(opp_scores)
                board.remove_checker(col)
        return scores
    def next_move(self, board):
        """returns the called AIPlayer's judgment of its best possible move
            input: board is a Board object.
        """
        self.num_moves += 1
        scores = self.scores_for(board)
        return self.max_score_column(scores)
    
                
                
        
        
        
    
    
    
