Game Rules:

1.The game involves moving game pieces on a grid and breaking squares of ice.
Players take turns moving their pieces and breaking ice squares.
The goal is to enclose the opponent so they cannot move.

2.Program Structure and Game Logic:
The main program includes a GUI loop and functions for various tasks.
Constants, variables, and graphics are initialized at the beginning.
The GUI loop handles mouse clicks and responds accordingly.

3.Program Constants:
3WINDOW_WIDTH: Width of the main application window.
WINDOW_HEIGHT: Height of the main application window.
BOARD_ROWS: Number of rows on the game board.
BOARD_COLUMNS: Number of columns on the game board.

4.Global Variables:
player: Identifies the player whose turn it is.
players: Dictionary containing player details and positions.
board: 2D list representing the state of each board square.

5.Function List:
setup_board(): Sets up the initial game board with squares.
display_player_status(player, task): Displays the player status message.
display_mouse_click_status(message): Displays the mouse click status message.
(Add more functions as you progress through milestones)

6.Milestone 1 Progress:
Implemented the basic structure of the program.
Created a main application window, set up the initial game board, and displayed status messages.
Implemented the GUI loop to handle mouse clicks.

7.Documentation, Comments, and Style:
Docstrings have been added for functions to explain their purpose.
Code includes comments for better readability.

8. Player Actions and Turns:
   a) Players can either move their game pieces or break ice squares on their turns.
   b) The game tracks the current player, and each player has specific actions to perform.
   c) After completing both move and break actions, the turn switches to the other player.

9. Move Piece Logic:
   a) The 'can_move_piece' function checks if the clicked square is a valid move for the current player.
   b) The 'move_piece' function updates the player's position on the board.
   c) The game board and player status are then updated accordingly.

10. Break Ice Logic:
   a) The 'can_break_ice' function checks if the clicked square is a valid ice-breaking move.
   b) The 'break_ice' function changes the color of the clicked square to indicate a broken ice square.
   c) The player status is updated to reflect the completed action.

11. Switching Players:
   a) The 'switch_player' function changes the current player to the other player after completing both actions.
   b) This ensures that players take turns, and the game progresses smoothly.

12. Update Board Function:
   a) The 'update_board' function redraws the game board based on the current player positions.
   b) It is called after each move or ice-breaking action to reflect the updated state.

13. Resetting the Game:
   a) The 'reset_game' function undraws all elements on the window and initializes a new game.
   b) This allows players to start a new game after the current one is finished.

14. Quitting the Game:
   a) The 'quit_game' function closes the application window and terminates the program.
   b) It displays a farewell message in the console.