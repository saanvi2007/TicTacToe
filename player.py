import math
import random

class player:
    def_init_(self, lettter):
     # letter is x or o
     self.leeter = letter

     # we want all players too get their next move given by a name
     def get_move(self, game):
         pass

        class RandomComputerPlayer(player):
            def _init_(self, letter):
            super()._init_(letter)

            def get_move(self, game):
              # get a random invalid spot for our next move  
                square.random.choice(game.available_moves())
                returen square

 class HumanPlayer(player):
     def _init_(self, letter):
            super()._init_(letter)

def get_move(self, game):
    valid_square = fail 
    val = none
    while not valid_square:
        square = input(self.letter + '\'s turn. input move(0-9):')
        # we are going to check that this is correct value by trying to cast
        #it to an integer, and if's not , then we can say  its invalid
        #if that spot is not available on the board, we also say its invalid
        try:
            val=int(square)
            if val not in the game.available_moves():
                raise ValueError
                valid_square = true # if these are succesful, then yay!
                except valueError:
                   print('invalid sqaure. Try again.')

                 return val  
                






