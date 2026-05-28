class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        
        box = defaultdict(set)

        for r in board:
            row = set()
            for element in r:
                if element != '.':
                    if element not in row:
                        row.add(element)
                    else:
                        print("row issie")
                        return False
        
        for i in range(9):
            column = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] not in column:
                        column.add(board[j][i])
                    else:
                        print("column issue")
                        return False
            print(column)
        
        for i in range(9):
            for j in range(9):
                r,c = i//3, j//3
                x = (r,c,)
                if board[i][j] != '.':
                    if x in box.keys():
                        if board[i][j] in box[x]:
                            print(box[x])
                            return False
                        else:
                            box[x].add(board[i][j])
                    else:
                        box[x].add(board[i][j])


        
        return True

                    
        