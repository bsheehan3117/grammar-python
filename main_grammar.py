'''
  CS5001
  HW 6
  Brendan Sheehan
  This program takes user input as the name of a file,
  extracts the contents of the file into a single string.
  Using the get_grammar, produce, and draw functions, this program
  draws the final sequence via turtle.
  Precondition:
  If the file was not found, it should print an appropriate
  message and stop the program.
'''

import grammar
import draw_grammar

def main():

  # take user input as file name, print error message if invalid:
  try:
    file = input("Please enter a file name: ")
    with open(file, "r") as new_file:
      string = new_file.read()
  except IOError:
    print("Please run the program again with a valid file name")
    exit()

  # create dictionary
  my_dictionary = {}

  # create dictionary using get_grammar function
  my_dictionary = grammar.get_grammar(string)

  # create sequence using produce function
  sequence = grammar.produce(my_dictionary)

  # produce drawing in python turtle using draw function
  drawing = draw_grammar.draw(my_dictionary, sequence)
  
if __name__ == "__main__":
  main()
