from abc import ABC, abstractmethod
from models import Board, Symbol

class Rules(ABC):
    @abstractmethod
    def checkWin(self, board: Board, sym: Symbol):
        pass
    @abstractmethod
    def checkDraw(self, Board: Board):
        pass
    @abstractmethod
    def isValid(self, Board: Board):
        pass

class StandardRules(Rules):
    def checkWin(self, board: Board, sym: Symbol):
        mark = sym.getMark()
        size = board._size
        
        for r in range(size):
            if all(board.getCell(r, c).getMark() == mark for c in range(size)):
                return True
        
        for c in range(size):
            if all(board.getCell(r, c).getMark() == mark for r in range(size)):
                return True
            
        if all(board.getCell(i, i).getMark() == mark for i in range(size)):
            return True
        if all(board.getCell(i, size-1-i).getMark() == mark for i in range(size)):
            return True
        return False
    
    def checkDraw(self, board: Board):
        for r in range(board._size):
            for c in range(board._size):
                if board.isCellEmpty(r, c):
                    return False
        return True
    
    def isValid(self, board: Board, row: int, col: int):
        
        if row<0 or col<0 or row>=board._size or col>=board._size:
            return False
        return  board.isCellEmpty(row, col)
    