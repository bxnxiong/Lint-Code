class Solution:
    # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
    # @return nothing 
    def surroundedRegions(self, board):
        # Write your code here
        connected = []
        res = []
        if len(board) > 0:
            rows = len(board)
            cols = len(board[0])
            visited = [[0]*cols for r in range(rows)]
            
            for r in [0,rows-1]: # only check first and last row
                for c in range(cols):
                    if board[r][c] == "O":
                        connected.append((r,c))
                        visited[r][c] = 1
            
            for c in [0,cols-1]: # only check first and last col
                for r in range(rows):
                    if board[r][c] == "O":
                        connected.append((r,c))
                        visited[r][c] = 1
            
            res = connected[:]
            
            while connected != []:
                r,c = connected.pop()
                
                for i in range(cols):
                    if visited[r][i] != 1 and abs(c-i) == 1 and board[r][i]=="O":
                        visited[r][i] = 1
                        connected.append((r,i))
                        res.append((r,i))
                
                for i in range(rows):
                    if visited[i][c] != 1 and abs(r-i) == 1 and board[i][c]=="O":
                        visited[i][c] = 1
                        connected.append((i,c))
                        res.append((i,c))
        
            for r in range(rows):
                for c in range(cols):
                    if board[r][c] == 'O':
                        if (r,c) not in res:
                            board[r][c] = 'X'