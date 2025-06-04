class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validRows = bool
        validCols = bool

        for i in board:
            hmap = {}
            for j in i:
                if j == ".":
                    continue
                else:
                    if j in hmap:
                        return False
                    else:
                        hmap[j] = 1
        validRows = True
        # check columns
        for i in range(len(board[0])):
            hmap = {}
            for j in board:
                if j[i] == ".":
                    continue
                else:
                    if j[i] in hmap:
                        return False
                    else:
                        hmap[j[i]] = 1
        validCols = True
        # check boxes
        validBoxes = bool
        boxes = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
        for i in boxes:
            x = i[0]
            y = i[1]
            hmap = {}
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if board[i][j] == ".":
                        continue
                    else:
                        if board[i][j] in hmap:
                            return False
                        else:
                            hmap[board[i][j]] = 1
            print(hmap)
        validBoxes = True
        
        return validRows and validCols and validBoxes
