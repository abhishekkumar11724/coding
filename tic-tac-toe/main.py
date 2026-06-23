from models import Player, Board, Symbol
from strategies import Rules, StandardRules
from services import Game, GameFectory, ConsoleNotifier
from enums import GameType

if __name__ == '__main__':
    game = GameFectory.createGame(GameType.STANDARD, 3)
    notifer = ConsoleNotifier()
    game.addObserver(notifer)
    p1 = Player(id = 1, name = 'alice', symbol=Symbol('O'))
    p2 = Player(id = 2, name = 'bob', symbol=Symbol('X'))
    
    game.addPlayer(p=p1)
    game.addPlayer(p=p2)
    
    game.notify('game started')
    game._board.display()
    
    game.play(0, 0) # Alice
    game.play(1, 1) # Bob
    game.play(0, 1) # Alice
    game.play(2, 2) # Bob

    game.play(1, 1) # invalid move
    game.play(0, 2) # alice wins