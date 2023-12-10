
# Class to represent an artificial click on the board
class artificialClick:
    def __init__(self, row, clmn):
        self.x = clmn*100+50
        self.y = row*100+50

# Class to implement the XO bot
class XO_bot:
    player = 'O'
    def __init__(self, game):
        self.game = game

    # Minimax algorithm for determining the best move
    def miniMax(self, _board, _turn):
        board = list(_board)
        
        # Check if there is a winner
        winner, lst = self.game.checkBoard(board)
        if winner:
            if winner == self.player:
                return 1
            else:
                return -1
        
        # Check if the board is full
        isFull = all(all(i != '' for i in _) for _ in board)
        if isFull:
            return 0
        
        # Recursively evaluate possible moves
        next_turn = {'X':'O', 'O':'X'}
        function, val = (max, -50000) if _turn == self.player else (min, 50000)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '':
                    board[i][j] = _turn
                    getted = self.miniMax(list(board), next_turn[_turn])
                    val = function(val, getted)
                    board[i][j] = ''
        return val

    # Make a move for the bot
    def makeMove(self, cnvs, brd, turn):
        if turn != self.player:
            return
        val = -50000
        nextMove = None
        
        # Find the best move by evaluating possible moves
        for i in range(len(brd)):
            for j in range(len(brd[0])):
                if brd[i][j] == '':
                    brd[i][j] = self.player
                    calc = self.miniMax(list(brd), 'X')
                    brd[i][j] = ''
                    if calc > val:
                        val = calc
                        nextMove = (i, j)
        if nextMove:
            self.game.click(artificialClick(nextMove[0], nextMove[1]))