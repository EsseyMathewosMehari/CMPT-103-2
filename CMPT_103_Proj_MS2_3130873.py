import time
import tkinter as tk
from graphics import GraphWin, Point, Rectangle, Text

class IcebreakerGame:
    """Icebreaker game implementation using graphics.py library."""

    def __init__(self):
        """
        Initialize the IcebreakerGame.

        1. Define game constants
        2. Initialize variables for the current player and player locations
        3. Create a GraphWin object for the main application window
        4. Set up the board with players in starting locations
        5. Create Text objects for player status and mouse click status messages
        6. Create Quit and Reset buttons
        7. Set up the main GUI loop
        """
        # Game Constants
        self.window_size = (600, 600)
        self.board_dim = (5, 5)

        # Player Information
        self.current_player = "Red"
        self.player_locations = {"Red": Point(0, 0), "Blue": Point(4, 4)}

        # Create the main application window
        self.win = GraphWin("Essey's Icebreaker", *self.window_size)

        # Set up the board with players in starting locations
        self.board = self.create_board_with_players()

        # Create Text objects for player status and mouse click status messages
        self.player_status_text = Text(Point(self.window_size[0] / 2, 20), "")
        self.mouse_status_text = Text(Point(self.window_size[0] / 2, self.window_size[1] - 20), "")
        self.update_player_status()

        # Create Quit and Reset buttons
        self.quit_button = Rectangle(Point(20, self.window_size[1] - 40), Point(80, self.window_size[1] - 20))
        self.quit_text = Text(Point(50, self.window_size[1] - 30), "QUIT")
        self.quit_button.draw(self.win)
        self.quit_text.draw(self.win)

        self.reset_button = Rectangle(Point(320, self.window_size[1] - 40), Point(380, self.window_size[1] - 20))
        self.reset_text = Text(Point(350, self.window_size[1] - 30), "RESET")
        self.reset_button.draw(self.win)
        self.reset_text.draw(self.win)

        # Set up the main GUI loop
        self.main_gui_loop()

    def create_board_with_players(self):
        """Create the game board with players in starting locations."""
        board = []
        for row in range(self.board_dim[0]):
            for col in range(self.board_dim[1]):
                player_piece = None
                for player, location in self.player_locations.items():
                    if location == Point(col, row):
                        player_piece = player
                        break
                square = Rectangle(Point(col, row), Point(col + 1.0, row + 1.0))
                square.setFill(player_piece.lower() if player_piece else "white")
                square.draw(self.win)
                board.append(square)
        return board

    def update_player_status(self):
        """Update the player status text on the window."""
        self.player_status_text.setText(f"Current Player: {self.current_player}")
        self.player_status_text.draw(self.win)

    def main_gui_loop(self):
        """Main GUI loop to handle user interactions."""
        while True:
            # Display whose move it is and which click is expected
            self.mouse_status_text.setText(f"{self.current_player}'s move. Click to move or break ice.")
            self.mouse_status_text.draw(self.win)

            click_point = self.win.getMouse()
            col, row = int(click_point.getX()), int(click_point.getY())

            # Check if Quit button is clicked
            if 20 <= col <= 80 and self.window_size[1] - 40 <= row <= self.window_size[1] - 20:
                self.quit_game()

            # Check if Reset button is clicked
            elif 320 <= col <= 380 and self.window_size[1] - 40 <= row <= self.window_size[1] - 20:
                self.reset_game()

            # Check if a board square is clicked
            elif 0 <= col < self.board_dim[1] and 0 <= row < self.board_dim[0]:
                if self.can_move_piece(col, row):
                    self.move_piece(col, row)
                elif self.can_break_ice(col, row):
                    self.break_ice(col, row)
                else:
                    self.mouse_status_text.setText("NOT VALID")
                    self.mouse_status_text.draw(self.win)
                    time.sleep(1)  # Display 'NOT VALID' for a short duration

            # Click elsewhere, display 'NOT VALID'
            else:
                self.mouse_status_text.setText("NOT VALID")
                self.mouse_status_text.draw(self.win)

            # Switch turns to the other player
            self.switch_player()

    def can_move_piece(self, col, row):
        """Check if the clicked square is a valid move for the current player."""
        # Implement your logic for checking if the piece can be moved
        return True

    def move_piece(self, col, row):
        """Move the game piece to the clicked square."""
        # Implement your logic for moving the piece
        self.player_locations[self.current_player] = Point(col, row)
        self.update_board()
        self.update_player_status()

    def can_break_ice(self, col, row):
        """Check if the clicked square is a valid ice-breaking move for the current player."""
        # Implement your logic for checking if ice can be broken
        return True

    def break_ice(self, col, row):
        """Break the ice in the clicked square."""
        # Implement your logic for breaking the ice
        self.board[row * self.board_dim[1] + col].setFill("white")
        self.update_player_status()

    def switch_player(self):
        """Switch turns to the other player."""
        self.current_player = "Red" if self.current_player == "Blue" else "Blue"

    def update_board(self):
        """Update the game board based on player locations."""
        for square in self.board:
            square.undraw()
        self.board = self.create_board_with_players()

    def reset_game(self):
        """Reset the game."""
        self.player_status_text.undraw()
        self.mouse_status_text.undraw()
        self.quit_button.undraw()
        self.quit_text.undraw()
        self.reset_button.undraw()
        self.reset_text.undraw()
        for square in self.board:
            square.undraw()
        self.__init__()

    def quit_game(self):
        """Quit the game."""
        self.win.close()
        print("BYE BYE !!")
        exit()

if __name__ == "__main__":
    game = IcebreakerGame()