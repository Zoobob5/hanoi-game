Towers of Hanoi Game

Welcome to the Towers of Hanoi game implemented in Python! This game challenges you to move a set of disks from one stack to another following specific rules.
Description

The Towers of Hanoi is a classic puzzle that consists of three rods and a number of disks of different sizes. The puzzle starts with all the disks stacked in ascending order of size on one rod, the smallest at the top, making a conical shape.

The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:

    Only one disk can be moved at a time.
    Each move consists of taking the top disk from one of the stacks and placing it on top of another stack.
    No disk may be placed on top of a smaller disk.

This implementation provides an interactive command-line interface for playing the game.
How to Play

    Setup:
        Run the script to start the game.
        You will be prompted to enter the number of disks you want to play with (minimum 3 disks).

    Game Play:
        The game displays the current state of the stacks.
        You will be prompted to enter the stack from which you want to move a disk and the stack to which you want to move the disk.
        The game will validate your move. If the move is invalid (e.g., moving from an empty stack or placing a larger disk on a smaller one), you will be prompted to try again.

    Winning:
        The game continues until all disks are moved from the left stack to the right stack.
        The game will then display the number of moves you took and compare it with the optimal number of moves.

Code Overview

The main script is structured as follows:

    Creating Stacks: Three stacks (left_stack, middle_stack, right_stack) are created using the Stack class.
    Setting Up the Game: The user is prompted to enter the number of disks. Disks are then pushed onto the left_stack.
    Printing Stacks: The print_stacks function prints the current state of all stacks.
    User Input: The get_input function handles user input for selecting stacks.
    Game Loop: The main loop handles the game logic, checking for valid moves and performing the disk moves until the puzzle is solved.

Files

    main.py: The main script to run the game.
    stack.py: Contains the Stack class definition.
    node.py: Contains the Node class definition used by the Stack class.
    
Sample look


    How many disks do you want to play with?
    3

    ...Current Stacks...
    Left Stack: [3, 2, 1]
    Middle Stack: []
    Right Stack: []

    Which stack do you want to move from?
    Enter L for Left
    Enter M for Middle
    Enter R for Right
    L

    Which stack do you want to move to?
    Enter L for Left
    Enter M for Middle
    Enter R for Right
    R

    Moved disk 1 from Left to Right

    ...Current Stacks...
    Left Stack: [3, 2]
    Middle Stack: []
    Right Stack: [1]
    
Bonus
change the winning messages.

