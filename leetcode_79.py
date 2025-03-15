class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows, self.cols = len(board), len(board[0])
        self.board = board
        self.word = word

        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == self.word[0]:  # Start DFS if first letter matches
                    if self.dfs(i, j, 0):
                        return True

        return False

    def dfs(self, r: int, c: int, index: int) -> bool:
        if index == len(self.word):  # If we found the entire word
            return True
        
        if (r < 0 or r >= self.rows or c < 0 or c >= self.cols or 
            self.board[r][c] != self.word[index]):
            return False

        # Temporarily mark the cell as visited
        temp = self.board[r][c]
        self.board[r][c] = "#"

        # Explore all four directions
        found = (self.dfs(r+1, c, index+1) or
                 self.dfs(r-1, c, index+1) or
                 self.dfs(r, c+1, index+1) or
                 self.dfs(r, c-1, index+1))

        # Restore the cell (backtracking)
        self.board[r][c] = temp
        return found
