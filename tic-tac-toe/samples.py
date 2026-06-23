

# from enum import Enum
# from typing import List, Optional

# # ==========================================
# # 1. ENUMS & EXCEPTIONS
# # ==========================================
# class PieceType(Enum):
#     X = "X"
#     O = "O"
#     EMPTY = "-"

# class GameStatus(Enum):
#     IN_PROGRESS = "IN_PROGRESS"
#     WON = "WON"
#     DRAW = "DRAW"

# class InvalidMoveException(Exception):
#     pass

# # ==========================================
# # 2. MODELS / ENTITIES
# # ==========================================
# class Player:
#     def __init__(self, name: str, piece: PieceType):
#         self.name = name
#         self.piece = piece

# class Board:
#     def __init__(self, size: int):
#         self.size = size
#         # Initialize an N x N grid with EMPTY pieces
#         self.grid = [[PieceType.EMPTY for _ in range(size)] for _ in range(size)]

#     def print_board(self):
#         print("\n--- Tic Tac Toe ---")
#         for row in self.grid:
#             print(" | ".join([cell.value for cell in row]))
#         print("-------------------\n")

#     def is_full(self) -> bool:
#         for row in self.grid:
#             for cell in row:
#                 if cell == PieceType.EMPTY:
#                     return False
#         return True

# # ==========================================
# # 3. SERVICES / MANAGERS (The Brains)
# # ==========================================
# class GameEngine:
#     def __init__(self, players: List[Player], board_size: int = 3):
#         self.board = Board(board_size)
#         self.players = players
#         self.current_turn = 0
#         self.status = GameStatus.IN_PROGRESS

#     def make_move(self, row: int, col: int):
#         if self.status != GameStatus.IN_PROGRESS:
#             print("Game is already over.")
#             return

#         # Edge Case: Out of bounds
#         if row < 0 or row >= self.board.size or col < 0 or col >= self.board.size:
#             raise InvalidMoveException(f"Move ({row}, {col}) is out of bounds.")

#         # Edge Case: Spot already taken
#         if self.board.grid[row][col] != PieceType.EMPTY:
#             raise InvalidMoveException(f"Spot ({row}, {col}) is already taken.")

#         # Place piece
#         current_player = self.players[self.current_turn]
#         self.board.grid[row][col] = current_player.piece
#         print(f"{current_player.name} placed {current_player.piece.value} at ({row}, {col})")
        
#         self.board.print_board()

#         # Check for win or draw
#         if self._check_winner(row, col, current_player.piece):
#             self.status = GameStatus.WON
#             print(f"🎉 {current_player.name} WINS! 🎉")
#         elif self.board.is_full():
#             self.status = GameStatus.DRAW
#             print("🤝 It's a DRAW! 🤝")
#         else:
#             # Pass turn to the next player
#             self.current_turn = (self.current_turn + 1) % len(self.players)

#     def _check_winner(self, last_row: int, last_col: int, piece: PieceType) -> bool:
#         """
#         O(N) time complexity. We only check the row, col, and diagonals 
#         of the LAST move made, rather than scanning the whole board.
#         """
#         size = self.board.size

#         # 1. Check Row
#         if all(self.board.grid[last_row][c] == piece for c in range(size)):
#             return True
            
#         # 2. Check Column
#         if all(self.board.grid[r][last_col] == piece for r in range(size)):
#             return True

#         # 3. Check Main Diagonal (only if the move was on it)
#         if last_row == last_col:
#             if all(self.board.grid[i][i] == piece for i in range(size)):
#                 return True

#         # 4. Check Anti-Diagonal (only if the move was on it)
#         if last_row + last_col == size - 1:
#             if all(self.board.grid[i][size - 1 - i] == piece for i in range(size)):
#                 return True

#         return False

# # ==========================================
# # 4. DRIVER CODE (The Final 5 Mins)
# # ==========================================
# if __name__ == "__main__":
#     # Setup Players
#     p1 = Player("Alice", PieceType.X)
#     p2 = Player("Bob", PieceType.O)

#     # Initialize Game (3x3)
#     game = GameEngine([p1, p2], board_size=3)

#     # Simulate a game (Hardcoding moves is faster than building a `while input()` loop during interviews)
#     try:
#         game.make_move(0, 0) # Alice
#         game.make_move(1, 1) # Bob
#         game.make_move(0, 1) # Alice
#         game.make_move(2, 2) # Bob
#         game.make_move(0, 2) # Alice wins on top row!
        
#         # This will trigger the "Game is already over" check
#         game.make_move(1, 0) 
        
#     except InvalidMoveException as e:
#         print(f"Error: {e}")



# =============================================================================

from enum import Enum
from collections import deque
from abc import ABC, abstractmethod
from typing import List

# ==========================================
# 1. ENUMS & EXCEPTIONS
# ==========================================
class GameType(Enum):
    STANDARD = "STANDARD"

class InvalidMoveException(Exception):
    pass

# ==========================================
# 2. MODELS / ENTITIES (Pure Nouns)
# ==========================================
class Symbol:
    def __init__(self, mark: str):
        self.mark = mark

    def get_mark(self) -> str:
        return self.mark

class Player:
    def __init__(self, id: int, name: str, symbol: Symbol):
        self.id = id
        self.name = name
        self.symbol = symbol
        self.score = 0  # From UML

class Board:
    def __init__(self, size: int):
        self.size = size
        self.empty_cell = Symbol('-')
        # vector<vector<Symbol>> in UML -> List of Lists in Python
        self.grid = [[self.empty_cell for _ in range(size)] for _ in range(size)]

    def is_cell_empty(self, row: int, col: int) -> bool:
        return self.grid[row][col] == self.empty_cell

    def place_mark(self, row: int, col: int, symbol: Symbol):
        if self.is_cell_empty(row, col):
            self.grid[row][col] = symbol
        else:
            raise InvalidMoveException(f"Cell ({row}, {col}) is already occupied.")

    def get_cell(self, row: int, col: int) -> Symbol:
        return self.grid[row][col]

    def display(self):
        print("\n--- Board ---")
        for row in self.grid:
            print(" | ".join([s.get_mark() for s in row]))
        print("-------------\n")


# ==========================================
# 3. STRATEGIES (The Rules Engine)
# ==========================================
class Rules(ABC):
    @abstractmethod
    def is_valid_move(self, board: Board, r: int, c: int) -> bool:
        pass

    @abstractmethod
    def check_win(self, board: Board, symbol: Symbol) -> bool:
        pass

    @abstractmethod
    def check_draw(self, board: Board) -> bool:
        pass

class StandardRules(Rules):
    def is_valid_move(self, board: Board, r: int, c: int) -> bool:
        # Check bounds
        if r < 0 or r >= board.size or c < 0 or c >= board.size:
            return False
        return board.is_cell_empty(r, c)

    def check_win(self, board: Board, symbol: Symbol) -> bool:
        mark = symbol.get_mark()
        size = board.size

        # Check rows
        for r in range(size):
            if all(board.get_cell(r, c).get_mark() == mark for c in range(size)):
                return True
                
        # Check columns
        for c in range(size):
            if all(board.get_cell(r, c).get_mark() == mark for r in range(size)):
                return True
                
        # Check diagonals
        if all(board.get_cell(i, i).get_mark() == mark for i in range(size)):
            return True
        if all(board.get_cell(i, size - 1 - i).get_mark() == mark for i in range(size)):
            return True

        return False

    def check_draw(self, board: Board) -> bool:
        # If any cell is empty, it's not a draw yet
        for r in range(board.size):
            for c in range(board.size):
                if board.is_cell_empty(r, c):
                    return False
        return True


# ==========================================
# 4. SERVICES / MANAGERS (Game & Observers)
# ==========================================
class IObserver(ABC):
    @abstractmethod
    def update(self, msg: str):
        pass

class ConsoleNotifier(IObserver):
    def update(self, msg: str):
        # The specific implementation of the Observer
        print(f"🔔 [NOTIFY]: {msg}")

class Game:
    def __init__(self, board: Board, rules: Rules):
        self.board = board
        self.rules = rules
        self.players = deque()       # deque<Player> from UML
        self.observers: List[IObserver] = [] 
        self.game_over = False

    def add_player(self, p: Player):
        self.players.append(p)

    def add_observer(self, o: IObserver):
        self.observers.append(o)

    def notify(self, msg: str):
        for observer in self.observers:
            observer.update(msg)

    def play(self, row: int, col: int):
        """
        Simulates a single turn. In a real game loop, this would be called repeatedly.
        """
        if self.game_over:
            self.notify("The game is already over!")
            return

        current_player = self.players[0]

        # 1. Validate Move using Strategy
        if not self.rules.is_valid_move(self.board, row, col):
            self.notify(f"Invalid move by {current_player.name} at ({row}, {col})")
            return

        # 2. Execute Move
        try:
            self.board.place_mark(row, col, current_player.symbol)
            self.notify(f"{current_player.name} placed '{current_player.symbol.get_mark()}' at ({row}, {col})")
            self.board.display()
        except InvalidMoveException as e:
            self.notify(str(e))
            return

        # 3. Check Game State using Strategy
        if self.rules.check_win(self.board, current_player.symbol):
            self.game_over = True
            current_player.score += 1
            self.notify(f"🎉 {current_player.name} wins the game!")
            return

        if self.rules.check_draw(self.board):
            self.game_over = True
            self.notify("🤝 The game ended in a draw.")
            return

        # 4. Rotate turns (pop from left, append to right)
        self.players.append(self.players.popleft())


class GameFactory:
    @staticmethod
    def create_game(game_type: GameType, size: int) -> Game:
        if game_type == GameType.STANDARD:
            board = Board(size)
            rules = StandardRules()
            return Game(board, rules)
        raise ValueError("Unknown Game Type provided to Factory")


# ==========================================
# 5. DRIVER CODE
# ==========================================
if __name__ == "__main__":
    # 1. Use the Factory to build the Game
    game = GameFactory.create_game(GameType.STANDARD, 3)

    # 2. Attach Observers
    notifier = ConsoleNotifier()
    game.add_observer(notifier)

    # 3. Create and add Players
    p1 = Player(id=1, name="Alice", symbol=Symbol("X"))
    p2 = Player(id=2, name="Bob", symbol=Symbol("O"))
    
    game.add_player(p1)
    game.add_player(p2)

    # 4. Simulate the gameplay
    game.notify("Game Started!")
    game.board.display()

    # Move sequence (Alice wins on the top row)
    game.play(0, 0) # Alice
    game.play(1, 1) # Bob
    game.play(0, 1) # Alice
    game.play(2, 2) # Bob
    
    # Invalid move test (spot taken)
    game.play(1, 1) # Alice tries to take Bob's spot -> Triggers Observer notification
    
    game.play(0, 2) # Alice wins!