def sudoku(board):
    
    def check(board, row, col, digit):
     
        for i in range(9):
            if board[row][i] == digit:
                return False
      
        for i in range(9):
            if board[i][col] == digit:
                return False
           
        startrow = (row//3) * 3
        startcol = (col//3) * 3
      
        for i in range(3):
            for j in range(3):
                if board[startrow+i][startcol+j] == digit:
                    return False

        return True

    def backtrack(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for digit in '123456789':
                        if check(board, row, col, digit):
                            board[row][col] = digit
                            if backtrack(board):
                                return True
                            board[row][col] = '.'  
                    return False

        return True 

    backtrack(board)
    return board

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]


result = sudoku(board)
for row in result:
    print(row)















































































































# def sudoku(board):
    
#     def isvalid(board,r,c,digit):
#         for i in range(9):
#             if board[r][i]==digit:
#                 return False
            
#         for i in range(9):
#             if board[c][i]==digit:
#                 return False
            
#         #print("TOO CHEKKK",board[c][i])
#         startrow = (r//3) *3
#         startcol = (c//3) *3
#         for i in range(3):
#             for j in range(3):
#                 if board[startrow+i][startcol+j]==digit:
#                     return False
                
#         return True
    
#     def backtrack(board):
#         for r in range(9):
#             for c in range(9):
#                 if board[r][c]==".":
#                     for digit in '123456789':
#                         if isvalid(board,r,c,digit):
#                             board[r][c]=digit
#                             if backtrack(board):
#                                 return True
#                             board[r][c] = "." 
#                     return False
#         return True   
#     backtrack(board)
#     return board

# board = [["5","3",".",".","7",".",".",".","."],
#          ["6",".",".","1","9","5",".",".","."],
#          [".","9","8",".",".",".",".","6","."],
#          ["8",".",".",".","6",".",".",".","3"],
#          ["4",".",".","8",".","3",".",".","1"],
#          ["7",".",".",".","2",".",".",".","6"],
#          [".","6",".",".",".",".","2","8","."],
#          [".",".",".","4","1","9",".",".","5"],
#          [".",".",".",".","8",".",".","7","9"]
# ]

# result = sudoku(board)
# for r in result:
#     print(r)