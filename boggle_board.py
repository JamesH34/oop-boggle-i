"""
1. create a 4x4 board
2. "shake" method that fills each space in the board with a
    random capital letter A-Z. this will require import random
    - shake should be a for or a for each type loop
3. 
"""
import random
import string

class BoggleBoard:
  #create a board that is 4 spaces x 4 spaces
  def __init__(self):
   self.blank_row = [
     ["_", "_", "_", "_"],
     ["_", "_", "_", "_"],
     ["_", "_", "_", "_"],
     ["_", "_", "_", "_"]
   ]
   for row in self.blank_row:
      print("".join(row))

   
  def shake(self):
    for row in range(4):
      for character in range(4):
      #  self.blank_row[row][character] = random.choice(string.ascii_uppercase)
       self.blank_row[row][character] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for row in self.blank_row:
      print("".join(row))
        




james = BoggleBoard()

james.shake()
james.shake()

# james.show_board()