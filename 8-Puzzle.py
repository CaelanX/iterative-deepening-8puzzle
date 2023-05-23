# Program: 8 - Puzzle Problem using Iterative Deepening Search
# Author: Caelan Neumann
# Description: A recursive implementation of Iterative deepening search
# based on the Pseudo-code from Artificial Intelligence: A Modern Approach by Peter Norvig and Stuart Russel
# Read the ReadMe.md for information on how to run
import random

#Create Node class
class Node:
    def __init__(self, state, parent, path, action):
      self.STATE = state
      self.PARENT = parent
      self.PATH = path
      self.ACTION = action


#define the constant goal state
goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

def populate_board():
    # Define our 3 X 3 board
    rows, columns = 3, 3
    board = [[0 for i in range(rows)] for j in range(columns)]
    #zero represents the blank tile
    problem_set = [0,1,2,3,4,5,6,7,8]
    
    #shuffle array to the start state
    random.shuffle(problem_set)
    
    insert_index = 0
    #insert the corresponding numbers into the board
    for i in range(rows):
        for j in range(columns):
            board[i][j] = problem_set[insert_index]
            insert_index = insert_index + 1

    return board


#find the index of zero
def find_blank(board):
    for i in range(3):
        for j in range(3):
            if 0 == board[i][j]:
                return i,j


#Gets the legal moves for current state
def get_moves(state):
    blank_row, blank_column = find_blank(state)
    moves = []
    #check if square can move up
    if blank_row > 0:
        moves.append('up')
    #check if square can move down
    if blank_row < 2:
        moves.append('down')
    #check if square can move left
    if blank_column > 0:
        moves.append('left')
    #check if square can move right
    if blank_column < 2:
        moves.append('right')
    return moves

#Check goal state
def check_goal(state):
    if state == goal:
        return True
    return False

def move_tile(state, move):
    #create a copy of the state
    move_state = [row[:] for row in state]
    #find zero
    blank_row, blank_column = find_blank(move_state)
    #apply upward movement
    if move == 'up':
        move_state[blank_row][blank_column] = move_state[blank_row - 1][blank_column]
        move_state[blank_row - 1][blank_column] = 0
    #apply downward movement
    elif move == 'down':
        move_state[blank_row][blank_column] = move_state[blank_row + 1][blank_column]
        move_state[blank_row + 1][blank_column] = 0
    #apply left movement
    elif move == 'left':
        move_state[blank_row][blank_column] = move_state[blank_row][blank_column  - 1]
        move_state[blank_row][blank_column  - 1] = 0
    #apply right movement
    elif move == 'right':
        move_state[blank_row][blank_column] = move_state[blank_row][blank_column + 1]
        move_state[blank_row][blank_column + 1] = 0
    return move_state


def recursive_dls(n, limit):
    #check the goal state and return the goal node if found
    if check_goal(n.STATE):
        return n
    #check if we are have reached our depth limit
    if limit == 0:
        return None
    
    
    for move in get_moves(n.STATE):
        #Create the node for next state
        child_state = move_tile(n.STATE, move)
        child_node = Node(child_state, n, n.PATH + [move], (child_state, move))
        result = recursive_dls(child_node, limit - 1)
        if result is not None:
            return result
    
    return None


def iterative_deepening_search(problem):
    #depth of search increased each iteration
    depth = 0;
    #Create start node from initial problem state
    start_node = Node(problem, None, [], None)
    #Call until a result is found
    while True:
        result = recursive_dls(start_node, depth)
        
        if result is not None:
            return result
        depth += 1
      

if __name__ == '__main__':
    #Initial state to use, use the populate_board() method to return a random state.   
    initial_state = [[1, 0, 3], [4, 5, 6], [2, 7, 8]]
    print(initial_state)
    solution_node = iterative_deepening_search(initial_state)
    
    #Output the path found
    print(solution_node.PATH)
    #Output the solved state, will be same as goal.
    print(solution_node.STATE)
 

    




