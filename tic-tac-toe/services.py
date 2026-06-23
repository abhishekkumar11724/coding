from models import Board, Symbol, Player
from enums import GameType
from strategies import Rules, StandardRules
from collections import deque
from exceptions import InvalidMoveException

class Iobserver:
    def update(self, msg):
        pass

class ConsoleNotifier(Iobserver):
    def update(self, msg):
        print(msg)

class Game:
    _board = None
    _players = None
    _rules = None
    _observers = None
    
    def __init__(self, board: Board, rules: Rules):
        self._board = board
        self._rules = rules
        self._players = deque()
        self._observers: list[Iobserver] = []
        self._gameOver = False

    def addPlayer(self, p: Player):
        self._players.append(p)
    
    def addObserver(self, obs: Iobserver):
        self._observers.append(obs)
    
    def notify(self, msg):
        for ele in self._observers:
            ele.update(msg)
    
    def play(self, row:int, col: int):
        if self._gameOver:
            self.notify("The game is already over!")
            return

        currentPlayer = self._players[0]
        
        if not self._rules.isValid(self._board, row, col):
            self.notify(f"Invalid move by {currentPlayer._name} at {row}, {col}")
            return
        
        try:
            self._board.MarkCell(row, col, currentPlayer._symbol)
            self.notify(f"""{currentPlayer._name} placed {currentPlayer._symbol.getMark()} at ({row}, {col})""")
            self._board.display()
        except InvalidMoveException as e:
            self.notify(str(e))
            return
        
        if self._rules.checkWin(self._board, currentPlayer._symbol):
            self._gameOver = True
            currentPlayer._score += 1
            self.notify(f"{currentPlayer._name} wins the game!")
            return
        
        if self._rules.checkDraw(self._board):
            self._gameOver = True
            self.notify("the game is a draw")
            return 
        
        self._players.append(self._players.popleft())
    
class GameFectory:
    @staticmethod
    def createGame(gameType: GameType, size : int) -> Game:
        if gameType == GameType.STANDARD:
            nullSymbol = Symbol('-')
            board = Board(size)
            rules = StandardRules()
            return Game(board=board, rules=rules)
        raise ValueError("unknown Game Type provided")
    