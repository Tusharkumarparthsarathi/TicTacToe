"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x =0
    y =0
    
    for i in range(3):
       for j in range(3): 
          if board[i][j]==X:
              x+=1
          if board[i][j]==O:
              y+=1
    
    if(x==y==0 or x<=y):
        return X
    else :
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ans = set()
    explored = set()
    board2 = copy.deepcopy(board)
    for i in range(3):
       for j in range(3):
           if board2[i][j]==EMPTY and (i,j) not in explored:
               explored.add((i,j))
               ans.add((i,j))
               board[i][j]=EMPTY
               
    return ans


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0] and action[1] not in (0,1,2):
        raise Exception("Invalid action.")
    board2 = copy.deepcopy(board)
    p = player(board2)
    board2[action[0]][action[1]]=p
    
    return board2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    board2 = copy.deepcopy(board)
    
    for i in range(3):
        if board2[i][0]==board2[i][1]==board2[i][2]==X or board2[0][i]==board2[1][i]==board2[2][i]==X :
            return X
        elif board2[i][0]==board2[i][1]==board2[i][2]==O or board2[0][i]==board2[1][i]==board2[2][i]==O :
            return O
        
    if board2[0][0]==board2[1][1]==board2[2][2]==X or board2[0][2]==board2[1][1]==board2[2][0]==X :
        return X
    elif board2[0][0]==board2[1][1]==board2[2][2]==O or board2[0][2]==board2[1][1]==board2[2][0]==O :
        return O
    else :
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    board2 = copy.deepcopy(board)
    if winner(board2)==X or winner(board2)==O:
        return True
    else :
        for i in range(3):
           for j in range(3):
               if board2[i][j]==EMPTY:
                   return False
    
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    board2 = copy.deepcopy(board)
    if winner(board2)==X:
        return 1
    elif winner(board2)==O:
        return -1
    else:
        return 0

def maxValue(board):
    board2 = copy.deepcopy(board)
    if terminal(board2):
        return utility(board2)
    v = -10
    for action in actions(board2):
        v = max(v,minValue(result(board2, action)))
    return v

def minValue(board):
    board2 = copy.deepcopy(board)
    if terminal(board2):
        return utility(board2)
    v = 10
    for action in actions(board2):
        v = min(v,maxValue(result(board2, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    a=[]
    b=[]
    c=[]
    d=[]
    board2 = copy.deepcopy(board)
    if terminal(board2):
        return None
    p = player(board2)
    if p==X:
        for action in actions(board2):
            if terminal(result(board2, action)):
                return action
            a.append(minValue(result(board2, action)))
            b.append(action)
        print(a)
        print(b)
        ans = max(a)
        print("ans",ans)
        for i in range(len(a)):
            if a[i]==ans:
                return (b[i])
    
    elif p==O:
        for action in actions(board2):
            if terminal(result(board2, action)):
                return action
            c.append(maxValue(result(board2, action)))
            d.append(action)
        ans = min(c)
        for i in range(len(c)):
            if c[i]==ans:
                return (d[i])
            
            
            
            
            