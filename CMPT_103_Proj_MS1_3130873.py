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
        3. Create a GraphWin object for main application window
        4. Set up the board
        5. Create Text objects for the player status and mouse click status messages
        6. Create Quit and Reset buttons
        7. Set up main GUI loop
        """
        # Game Constants
        self.window_size = (600, 600)
        self.board_dim = (5, 5)

        # Player Information
        self.current_player = "Red"
        self.player_locations = {"Red": Point(0, 0), "Blue": Point(4, 4)}

        # Create the main application window
        self.win = GraphWin("Essey's Icebreaker", *self.window_size)

        # Set up the board
        self.board = self.create_board()

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

        # Set up main GUI loop
        self.main_gui_loop()

    def create_board(self):
        """Create the game board."""
        board = []
        for row in range(self.board_dim[0]):
            for col in range(self.board_dim[1]):
                square = Rectangle(Point(col, row), Point(col + 1, row + 1))
                square.draw(self.win)
                board.append(square)
        return board

    def update_player_status(self):
        """Update the player status text on the window."""
        self.player_status_text.setText(f"Current Player: {self.current_player}")
        self.player_status_text.draw(self.win)

    def main_gui_loop(self):
        """Main GUI loop to handle user interactions.

        The loop waits for a mouse click and performs the following actions:
        a) On clicking QUIT: Display 'BYE BYE!!', wait for one last mouse click,
           close the window, and terminate the program.
        b) On clicking RESET: Display “RESET” and return to the top of the GUI loop.
        c) On clicking on the board: Display (column, row) of the square clicked
           and return to the top of the GUI loop.
        d) On clicking elsewhere: Display 'NOT VALID' as the mouse click status message.
        """
        while True:
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
                self.display_square_clicked(col, row)

            # Click elsewhere, display 'NOT VALID'
            else:
                self.mouse_status_text.setText("NOT VALID")
                self.mouse_status_text.draw(self.win)

    def display_square_clicked(self, col, row):
        """Display the (column, row) of the square clicked.

        Parameters:
        - col (int): The column of the clicked square.
        - row (int): The row of the clicked square.
        """
        self.mouse_status_text.setText(f"Square Clicked: ({col}, {row})")
        self.mouse_status_text.draw(self.win)

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