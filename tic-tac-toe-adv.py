#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:11:34 2020

@author: sanantha
TIC TAC TOE GAME
Step1:
    Write a function that can print out a board. Setup your board as a list, 
    where each index 1-9 corresponds with a number on a number pad, so you get
    3 by 3 board representation
Step2:
    Write a function that can take a player input and assign their marker as
    'X' or 'O'. Think about using while loops to continually ask until you get
    a correct answer
Step3:
    Write a function that takes in the board list object, a marker ('X' or 'O')
    and a desired position (number 1-9) and assigns it to the board
Step4:
    Write a function that takes in a board and mark (X or O) and then checks
    to see if that mark has won

"""

from IPython.display import clear_output

board = [' ']*10
game_state = True
announce = ''

#Note: Game will ignore 0 index

def reset_board():
    global board, game_state
    board = [' ']*10
    game_state = True
    
def display_board():
    ''' 
    This function displays the board so that the numpad can be used as
    a reference
    '''
    # Clear the current cell output
    clear_output()
    #Print Board
    print ("  "+board[7]+" |"+board[8]+" | "+board[9]+" ")
    print ("-------------")
    print ("  "+board[4]+" |"+board[5]+" | "+board[6]+" ")
    print ("-------------")
    print ("  "+board[1]+" |"+board[2]+" | "+board[3]+" ")
    
def win_check(board, player):
    ''' Check Horizontals, Verticals and Diagonals for a win'''
    if (board[7] == board[8] == board[9] == player) or \
        (board[4] == board[5] == board[6] == player) or \
        (board[1] == board[2] == board[3] == player) or \
        (board[7] == board[4] == board[1] == player) or \
        (board[8] == board[5] == board[2] == player) or \
        (board[9] == board[6] == board[3] == player) or \
        (board[7] == board[5] == board[3] == player) or \
        (board[1] == board[5] == board[9] == player):
        
        return True
    else:
        return False

def full_board_check(board):
    ''' Function to check if any remaining blanks in the board '''
    
    if " " in board[1:]:
        return False
    else:
        return True
    
def ask_player(mark):
    ''' Ask player to place X or O mark, checks validity '''
    global board
    req = 'Choose where to place your ' + mark
    while True:
        try:
            choice = int(input(req))
        except ValueError:
            print('Sorry, please input a number between 1-9.')
            continue
        if board[choice] == " ":
            board[choice] = mark
            break
        else:
            print ("That space isn't empty")
            continue

def player_choice(mark):
    global board, game_state, announce
    #set game blank game announcement
    announce = ''
    mark = str(mark)
    #Validate input
    ask_player(mark)
    
    #Check for player win
    if win_check(board, mark):
        clear_output()
        display_board()
        announce = mark +" Wins! Congratulations!"
        game_state = False
    
    #Show output
    clear_output()
    display_board()
    
    #Check for tie
    if full_board_check(board):
        announce = "Tie!"
        game_state = False
    
    return game_state, announce

def play_game():
    reset_board()
    global announce
    
    #Set Marks
    X = 'X'
    O = 'O'
    
    while True:
        #Show board
        clear_output()
        display_board()
        
        # Player X turn
        game_state, announce = player_choice(X)
        print(announce)
        if game_state == False:
            break

        #Player O turn
        game_state, announce = player_choice(O)
        print(announce)
        if game_state == False:
            break            
        
    rematch = input('Would like to play again? y/n')
    if rematch == 'y':
        play_game()
    else:
        print('Thanks for playing!')

play_game()