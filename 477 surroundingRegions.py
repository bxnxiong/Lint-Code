class Solution:
    # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
    # @return nothing 
    def surroundedRegions(self, board):
        # Write your code here
        def fill(r,c):
            if r < 0 or r >= rows or c < 0 or c>= cols or board[r][c]!='O':return
            board[r][c] = 'f'
            connected.append((r,c))
        if len(board) > 0:
            rows = len(board);cols = len(board[0]);connected = []
            for c in range(cols):# only check first and last row
                fill(0,c);fill(rows-1,c)
            for r in range(rows):# only check first and last col
                fill(r,0);fill(r,cols-1)
            while connected != []:
                r,c = connected.pop()
                fill(r-1,c);fill(r+1,c);fill(r,c-1);fill(r,c+1)
            for r in range(rows):
                for c in range(cols):
                    if board[r][c] == 'f':board[r][c] = 'O'
                    elif board[r][c] == 'O':board[r][c] = 'X'