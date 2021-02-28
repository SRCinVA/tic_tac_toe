import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        # we will use a single list of length 9
        # that will represent the 3*3 board
        self.current_winner = None # to keep track of winner
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:  
        # Line 9 creates a slice (from "start" to "end," exclusive of "end")
        # Range() in Python is exclusive of user's input, so this encompasses 0,1,2
        # the range bracket creates three "self-contained" slices of indices, like this:
            # [0,1,2],[3,4,5],[6,7,8]
        # we make a list out of the elements, further divided into another list every third item.
        # it indexes into our len 9 list
        
            print('| ' + ' | '.join(row) + ' |')
            # print the first pipe; join() method intersperses the pipe between the iterables; print the last pipe.
    
    @staticmethod # static methods are methods bound to the class, not the object
    def print_board_nums(): # this doesn't relate to any specific board, so we don't have to pass in self (makes sense).
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        # inner list gives the indices present in a single row.
        # outer list gives all of the rows.
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # the long way to do it:
        # moves = []  # initialize moves to an empty list.
        # for (i,spot) in enumerate(self.board): # basically, it attaches an object to its index place.
        #     # ['x','x','o'] --> [(0,'x'),(1,'x'),(2,'o')]
        #     if spot == ' ':  # meaning that it's empty and available for use.
        #         moves.append(i)  # we append that index to know that it's been taken. 
        #         return moves
    
        # using list comprehension:
        return [i for i, spot in emumerate(self.board) if spot == ' ']
        # basically, this says: "when enumerating through (i, spot),
        # if the spot is empty, put it into this list." (where is 'moves' here?)

    def empty_squares(self):
        # return ' ' in self.board # this will just return a boolean if the selection is an empty space
        return self.board.count(' ') # she opted to just count the spaces in the board; seems easier


    # we might want to know the number of empty squares
    def num_empty_squares(self):
        return len(self.available_moves())
        # the above will retutn the available_moves list, and we can count the number of empty spots

    # to actually make a move
    def make_move(self, square, letter):
        # if we're going to make a move, then we need to be sure it's valid
        # If valid, it returns True; if not, then False
        if self.board[square] == ' ': # if that square on the board is empty ...
            self.board[square] = letter # ... then put the letter in that space.
            # now you need to check if you actually won (we'll do this later):
            if self.winner(square, letter): # passes in last move, but WTF did 'winner' come from??
                self.current_winner = letter
            return True
        else:
            return False

    def winner(self, square, letter):
        # we have to check all possibilities of three in a row.
        # first check the row
        row_ind = square // 3  # divide by three and then round down. Don't understand what this is achieving.
        row = self.board[row_ind*3 : (row_ind + 1)] # not at all clear what this is.
        if all([spot == letter for spot in row]):   # "spot" is just a name; the important thing is the list comprehension syntax.
                                                    # if all of these items are True ...
            return True
        
        # check columns
        col_ind = square % 3   # same (unclear) reasoning employed as above.
        column = [self.board[col_ind+1*3] for i in range(3)]  # a mystery ...
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]): # can use a similar checker
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all of these checks fail, then there's no winner, so it returns False
        return False

# notice that this function exists outside of the TicTacToe class
def play(game, x_player, o_player, print_game=True):
    if print_game: #meaning, if we want to see it
        game.print_board_nums # this way we can see which number corresonds to which spot.

    letter = "X" # a starting letter
    # iterate while the game has empty squares
    # (we don't have to worry about a winner because we'll
    # just return whatever breaks the loop).

    # she calls this "the play loop" (which makes sense):
    while game.empty_squares(): # for checking if the game has empty squares
        # while there are emptyspaces, let's get the next move from the appropriate player
        if letter == "0":
            square = o_player.get_move(game)
        else:
            square = x_player.getmove(game)

    # define a function to actually make a move
        if game.make_move(square, letter): # meaning, "is valid":
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board() # so that we can see what the user just did
                print('')

            if game.current_winner: # *seems* this serves as a checker to make sure there's no winner
                if print_game: # not sure why this line is needed
                    print(letter + ' wins!')
                return letter

            # after making a single move, we need to alternate letters
            # here, we assign the letter to 'O' if it's currently 'X',
            # otherwise, we just assign 'letter' to 'X' (don't even need the rest of the statement)
            letter = 'O' if letter 'X' == 'X' else 'X'
            # another way to do this is below (probably what I would have done):
            # if letter == 'X':
            #   letter = 'O'
            # else:
            #   letter = 'X' 

        # let's introduce a pause of 0.8 seconds
        time.sleep(0.8)


    if print_game: # here, if we fall out of the first loop, then there was no winner. 
        print("It\'s a tie!")

if __name__ == '__main__':  # What in the world is going on with this line? Can't you just set up __main__ as a standalone?
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe
    play(t, x_player, o_player, print_game=True)
