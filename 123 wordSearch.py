class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        # write your code here
        
        def dfs(r,c,word):
            if len(word) == 0: return True
            else:
                # up
                if r > 0 and board[r-1][c] == word[0]:
                    tmp = board[r][c];board[r][c] = '#'
                    if dfs(r-1,c,word[1:]):
                        return True
                    board[r][c] = tmp
                    
                # down
                if r < len(board)-1 and board[r+1][c] == word[0]:
                    tmp = board[r][c];board[r][c] = '#'
                    if dfs(r+1,c,word[1:]):
                        return True
                    board[r][c] = tmp
                    
                # left
                if c > 0 and board[r][c-1] == word[0]:
                    tmp = board[r][c];board[r][c] = '#'
                    if dfs(r,c-1,word[1:]):
                        return True
                    board[r][c] = tmp
                
                # right
                if c < len(board[0])-1 and board[r][c+1] == word[0]:
                    tmp = board[r][c];board[r][c] = '#'
                    if dfs(r,c+1,word[1:]):
                        return True
                    board[r][c] = tmp
                    
                return False
            
        if len(board) == 0:
            if word == "":
                return True
            else:
                return False
        else:
            for r in range(len(board)):
                for c in range(len(board[0])):
                    if board[r][c] == word[0]:
                        if dfs(r,c,word[1:]):
                            return True
            return False