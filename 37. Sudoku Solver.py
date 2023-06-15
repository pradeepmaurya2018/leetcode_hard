import collections
import os
from typing import List


def printList(grid):
    for i in range(len(grid)):
        print(*grid[i])

def printMapping(mapping):
    for m, n in mapping.items():
        print(m, n)


class Solution:
    os.remove("log.txt")
    file = open("log.txt", 'a')
    ans = None

    def logList(self, grid):
        for g in grid:
            self.file.writelines(f"{g}" +"\n")

    def canBeFilled(self, board, i, j, d, N, M):
        # print(i, j, d)
        for x in range(N):
            if board[i][x] == d:
                return False
        for x in range(M):
            if board[x][j] == d:
                return False

        row_start = (i // 3) * 3
        col_start = (j // 3) * 3

        for x in range(3):
            for y in range(3):
                if board[x + row_start][y + col_start] == d:
                    return False
        return True

    def goaheadAndpopulate(self, board, i, j, N, M, visited, mapping):
        self.solveSudokuUtil(board, i, j + 1, N, M, visited, mapping)
        # self.solveSudokuUtil(board, i + 1, j, N,
        #                      M, visited, mapping)
        # self.solveSudokuUtil(
        #     board,
        #     i + 1,
        #     j + 1,
        #     N, M, visited, mapping)
        # # visited[i][j] = 0

    def solveSudokuUtil(self, board, i, jj, N, M, visited, mapping):
        i = jj // N
        j = jj % M
        if 0 <= j < M * N:
            # visited[i][j] = 1
            # printList(board)

            # inp=input()


            if board[i][j] == ".":
                for d in range(1, 10):
                    # mapping[(i,j)].append(d)
                    # self.file.writelines(f"{i} {j} {d} " + str(board) + "\n")
                    # print(jj, i, j, d)
                    check = self.canBeFilled(board, i, j, chr(ord('0') + d), N, M)
                    # print(i, j, d, check)
                    if check:
                        board[i][j] = chr(ord('0') + d)
                        # if i == N - 1 and j == M - 1:
                        #     print("Reached end cell")
                        #     return
                        # self.file.writelines(str(jj) + "\n")

                        if jj == 80 and self.ans is None:
                            self.logList(board)
                            self.ans = board
                            return
                        self.goaheadAndpopulate(board, i, jj, N, M, visited, mapping)
                        board[i][j] = "."

                # visited[i][j]=0

            else:
                if jj == 80 and self.ans is None:
                    self.logList(board)
                    self.ans = board
                    return
                self.goaheadAndpopulate(board, i, jj, N, M, visited, mapping)
                # board[i][j] = "."
                # visited[i][j] = 0

    def solveSudoku(self, board: List[List[str]]):
        """
        Do not return anything, modify board in-place instead.
        """
        mapping = collections.defaultdict(list)
        N = len(board)
        M = len(board[0])
        # N, M = 6, 9
        visited = [[0 for _ in range(M)] for __ in range(N)]
        # print(self.canBeFilled(board,0,2,chr(ord('0') + 3), N, M))
        self.solveSudokuUtil(board, 0, 0, N, M, visited, mapping)
        # printMapping(mapping)
        print(self.ans)
        return self.ans


sol = Solution()
grid = sol.solveSudoku(
    [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
printList(grid)
# printList(visited)
