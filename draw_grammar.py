'''
    Brendan Sheehan
    CS5001
    Homework 6

    This file contains the draw function
'''

import turtle
b = turtle.Turtle()
def draw(grammar, sequence):
    '''
    Function: draw
    This function accepts the dictionary of the same format as created by the get_grammar function, and a sequence to be drawn (for example, one created by the produce function). This function should use Python's turtle package to open a window and draw the sequence according to the specifications in the dictionary (how much to go forward, how much to turn).
    Parameters: grammar
    (dictionary with key value pairs
    'symbols' -> sequence of symbols
    'start' -> starting sequence
    symbol eg. 'A' -> the expansion of that symbol for each rule in the file
    'angle' -> the angle in degrees as a number
    'draw-X' -> the distance to move forward for that symbol as
    a number (X replaced by symbol)
    'iterations' -> number of expansions to do as a number
    sequence: a string containing the sequence of symbols to be drawn
    Returns: No return, draws the sequence with turtle
    Pre-condition: Ignore symbols without a drawing rule
    '''

    # prepare turtle
    window = turtle.Screen()
    window_size = turtle.screensize(1200, 1200)
    b.penup()
    b.setpos(0,0)
    b.pendown()
    angle = int(grammar.get("angle"))
    
    # loop through each characters in sequence
    for character in sequence:

    # define directions for + and -
        if character == "+":
            b.left(angle)
        elif character == "-":
            b.right(angle)
        
        # if the character is in the dictionary, move based on value
        # move turtle forward and turn it according to the value
        else:
            key = "draw-" + character
            b.forward(int(grammar.get(key)))

