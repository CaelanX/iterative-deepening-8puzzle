import random

def populate_board():
    # Define our 3 X 3 board
    rows, columns = 3, 3
    board = [[0 for i in range(rows)] for j in range(columns)]
    #zero represents the blank tile
    problem_set = [0,1,2,3,4,5,6,7,8]
    #shuffle array to create the board
    random.shuffle(problem_set)
    
    insert_index = 0

    for i in range(rows):
        for j in range(columns):
            board[i][j] = problem_set[insert_index]
            insert_index = insert_index + 1

    return board



def find_blank(board):
    for i in range(3):
        for j in range(3):
            if 0 == board[i][j]:
                return i,j        


 

if __name__ == '__main__':

    initial_state = populate_board()
    print(initial_state)

    blank_row, blank_column = find_blank(initial_state)
    
    


    




