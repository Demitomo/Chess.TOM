# Chess.tom

The best chess game made entirely in python with the [pygame](https://github.com/pygame/) library !

## Functionalities
1. Display the pieces in any given positions
2. Move each pieces to a certain square
3. Uses the position of the mouse to select the pieces and where they should go to
4. Checks if the move is valid
5. (soon) Checks if the king is in check

## To-Dos
#### Assign the according possible movement to each of the pieces:
- [x] Knight Moves
- [x] Bishop Moves
- [x] Rook Moves
- [x] King Moves
- [x] Queen Moves
- [x] Pawn Moves/Takes
- [x] Pawn promotion
- [x] Castling (short and long)

#### Finds checks and checkmates:
- [ ] Verifies each turn if the king is in check
- [ ] Check if it is checkmate

#### Miscellaneous:
- [ ] End screen/play again screen
- [ ] Add a timer
- [ ] Ability to change the piece by clicking on it
- [x] Display the possible moves of a piece
- [ ] Save the game
- [ ] Use only one image for each piece (SVG) and fill it with the color of the player

## Functionalities of each file
1. index.py:
Game loop, display the board

2. pieces.py:
Loads the images and resizes them, creates the classes for each piece with their own specific movement

## How to run the game
1. Clone the repository
2. Install the requirements with `pip install -r requirements.txt`
3. Run the game with `python src/index.py`
4. Enjoy !

## Development
This project is still in development, if you want to contribute, feel free to fork the repository and make a pull request !

## Authors
- [Demitomo](https://github.com/Demitomo)  : Main developer of the application
- [pierrbt](https://github.com/pierrbt) : Helping with overall app workflow and code review
