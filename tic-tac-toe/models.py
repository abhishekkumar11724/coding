from exceptions import InvalidMoveException

class Symbol:
    mark = None
    def __init__(self, mark):
        self.mark = mark
        
    def getMark(self):
        return self.mark

class Board:
    _size = None
    _grid = None
    _nullCell = None
    
    def __init__(self, size):
        self._size = size
        self._nullCell = Symbol('-')
        self._grid = [[self._nullCell for _ in range(size)] for _ in range(size)]

    def isCellEmpty(self, row:int, col:int) -> bool:
        return self._grid[row][col] == self._nullCell
    
    def getCell(self, row:int, col:int) -> Symbol:
        return self._grid[row][col]
    
    def MarkCell(self, row:int, col:int, sym:Symbol):
        if self.isCellEmpty(row, col):
            self._grid[row][col] = sym
        else:
            raise InvalidMoveException(f"Cell ({row}, {col}) is already occupied.")
        
    def display(self):
        for i in range(self._size):
            for j in range(self._size):
                print(self._grid[i][j].getMark(), end="  ")
            print("\n")
            
        # print("\n--- Board ---")
        # for row in self._grid:
        #     print(" | ".join([s.get_mark() for s in row]))
        # print("-------------\n")

class Player:
    _id = None
    _name = None
    _symbol = None
    _score = None
    def __init__(self, id: int, name: str, symbol: Symbol):
        self._id = id
        self._name = name
        self._symbol = symbol
        self._score = 0
        
    def getData(self):
        data = {
            "name": self._name,
            "symbol": self._symbol,
            "id": self._id
        }
        return data