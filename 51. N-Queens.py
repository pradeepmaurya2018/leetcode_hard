from typing import List


class Solution:
    count = 0

    def isSafeVirtical(self, board, i, j, N):
        for x in range(N):
            if board[x][j] == "q":
                return False
        return True

    def isSafeHorizontal(self, board, i, j, N):
        for x in range(N):
            if board[i][x] == "q":
                return False
        return True

    def isSafeFirstDiagonal(self, board, ii, jj, N):
        i, j = ii, jj
        while (i >= 0 and j >= 0):
            if board[i][j] == "q":
                return False
            j -= 1
            i -= 1
        i, j = ii, jj

        while j < N and i < N:
            if board[i][j] == "q":
                return False
            i += 1
            j += 1
        return True

    def isSafeSecondDiagonal(self, board, ii, jj, N):
        i, j = ii, jj
        while i >= 0 and j < N:
            if board[i][j] == "q":
                return False
            j += 1
            i -= 1
        i, j = ii, jj

        while j >= 0 and i < N:
            # print("III ", i, j)
            if board[i][j] == "q":
                return False
            i += 1
            j -= 1
        return True

    def isSafe(self, board, i, j, N):
        return self.isSafeVirtical(board, i, j, N) and self.isSafeHorizontal(board, i, j,
                                                                             N) and self.isSafeFirstDiagonal(
            board, i, j, N) and self.isSafeSecondDiagonal(board, i, j, N)

    def solveNQueensUtil(self, board, jj, N):

        i = jj // N
        j = jj % N
        if i <= N - 1 and j <= N - 1:

            safe = self.isSafe(board, i, j, N)
            # print(i, j, safe)
            if safe:
                self.count += 1
                board[i][j] = "q"

            if i == N - 1 and j == N - 1:
                print(self.count, board)

            self.solveNQueensUtil(board, jj + 1, N)

    def solveNQueens(self, n: int) -> List[List[str]]:
        board=None
        for ii in range(64):
            self.count=0
            board = [["0" for j in range(n)] for i in range(n)]
            self.solveNQueensUtil(board, ii, n)
        return board

    def printBoard(self, board):
        for a in board:
            print(*a)


sol = Solution()
(sol.solveNQueens(8))
print(sol.count)
