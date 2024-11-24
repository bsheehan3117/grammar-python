'''
    CS5001
    HW 6
    Brendan Sheehan
    This file contains the get_grammar and produce functions
'''

def get_grammar(grammar_string):

    '''
    Function: get_grammar
    This function produces a dictionary from the contents of a grammar file.
    Parameters: grammar_string... the contents of a grammar file as a single string
    Returns: A dictionary containing entries with the following key value pairs...
    'symbols' -> sequence of symbols
    'start' -> starting sequence
    symbol eg. 'A' -> the expansion of that symbol for each rule in the file
    'angle' -> the angle in degrees as a number
    'draw-X' -> the distance to move forward for that symbol as a number (X replaced by symbol)
    'iterations' -> number of expansions to do as a number
    Pre-condition: If the string has format errors, should raise a ValueError
    Expected output for example.txt: {'symbols': 'AB+-', 'start': 'A', 'A': 'A+B-B+A', 'B': 'A+B', 'angle': 90, 'draw-A': 30, 'draw-B': 30, 'iterations': 3} 
    '''

    # split input into a list of strings
    new_string = grammar_string.split('\n')

    # create an empty dictionary
    dictionary = {}

    # for each element in the string, iterate through
    # and create keys and values from sublists
    for element in new_string:
        new_lst = element.split(' ')
        
    # lists longer than 2 elements search for draw and rule
    # merge draw with a '-' and the next element as pair
        if len(new_lst) > 2:
            if new_lst[0] == "draw":
                dictionary[new_lst[0] + '-' + new_lst[1]] = new_lst[2]
            if new_lst[0] == 'rule':
                dictionary[new_lst[1]] = new_lst[2]
        elif len(new_lst) > 1 and len(new_lst) < 3:
            dictionary[new_lst[0]] = new_lst[1]

    return dictionary


def produce(grammar):

    '''
    this function uses a dictionary to produce an expanded
    sequence of characters. It should start with
    the given starting symbol, expand it the number of specified
    times, and return the resulting final sequence.
    parameters: dictionary of the same format
    as created by the get_grammar function.
    returns: a final sequence.
    preconditions: If the dictionary does not contain a starting sequence,
    or a number of expansions then this function should raise a ValueError exception.
    '''
    
    # raise valueerror if file does not contain start or iterations
    if 'start' not in grammar: 
        raise ValueError('File does not contain start')
    if 'iterations' not in grammar:
        raise ValueError('File does not contain iterations')
    
    # define start and change iterations to int
    start = grammar['start']
    iterations = int(grammar['iterations'])
    sequence = start
    
    # for loop, for each iteration replace the character from
    # the dictionary with the expanded grammar 
    for i in range(iterations):
        new_sequence = ""
        for character in sequence:
            if character in grammar:
                new_sequence += grammar[character]
            else:
                new_sequence += character
        sequence = new_sequence
    
    return sequence
