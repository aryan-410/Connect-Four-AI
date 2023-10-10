# 🔴 Connect Four AI: Tactical Gameplay with Minimax 🟡

Welcome to the Connect Four AI repository! Dive into a classic game supercharged with the power of Minimax. This AI promises to challenge your Connect Four tactics, offering an opponent that thinks multiple moves ahead.

## 📖 Table of Contents
- [Game Class](#game-class)
- [Connect Four AI](#connect-four-ai)
- [How to Play](#how-to-play)
- [Contributions & Feedback](#contributions--feedback)

## 🎮 Game Class
Located in: `gameClass.py`

The `gameClass.py` serves as the foundation of our Connect Four game. It's responsible for the core mechanics of the game.

### Key Features:

- **State Management**: Keeps track of the current game state, including which cells are occupied.
- **Piece Movement**: Methods to place pieces on the board and validate legal moves.
- **Board Visualization**: Displays the board to the user in a clear and intuitive format.

## 🤖 Connect Four AI
Located in: `connect4Ai.py`

This is where the AI's tactical magic happens. Using the Minimax algorithm, the AI calculates optimal moves to either win or block the player.

### How It Works:

1. **Decision Tree**: For each possible column drop, a decision tree is generated. Each level of this tree represents potential game states after subsequent moves by the player and AI.
2. **Evaluating Moves**: The algorithm assigns scores to potential moves, predicting outcomes to select the best strategy.
3. **Depth-Limited Search**: To keep gameplay smooth, we limit the search depth, balancing between performance and strategy.

## 🎲 How to Play
Run the game using: `connectFour.py`

Jump into a tactical game of Connect Four by executing `connectFour.py`. This script merges the game mechanics and the AI to provide an interactive gaming experience.

### Instructions:

1. **Starting the Game**: Run `connectFour.py`.
2. **Making Moves**: Follow on-screen prompts to drop your piece into the desired column.
3. **Facing the AI**: After your move, watch the AI strategize and make its counter-move.

## 💌 Contributions & Feedback

Your insights and feedback are cherished! Should you find bugs, have feature suggestions, or wish to contribute, please open an issue or submit a PR. Let's elevate this Connect Four AI experience together!

🎉 Enjoy the challenge and happy gaming! 🎉
