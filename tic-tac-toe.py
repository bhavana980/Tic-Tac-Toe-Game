from tkinter import *
from tkinter import messagebox
import random

# Create window
root = Tk()
root.title("Tic Tac Toe - Me vs Computer")
root.geometry("400x500")
root.config(bg="lightblue")

# Variables
board = [""] * 9
buttons = []
player = "X"
computer = "O"


# Function to check winner
def check_winner():
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in winning_positions:
        a, b, c = combo

        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]

    if "" not in board:
        return "Tie"

    return None


# Computer move
def computer_move():
    empty_boxes = []

    for i in range(9):
        if board[i] == "":
            empty_boxes.append(i)

    if empty_boxes:
        move = random.choice(empty_boxes)

        board[move] = computer
        buttons[move].config(text=computer)

        winner = check_winner()

        if winner:
            if winner == "Tie":
                messagebox.showinfo("Game Over", "It's a Tie!")
            else:
                messagebox.showinfo(
                    "Winner",
                    f"Player {winner} Wins!"
                )
            reset_game()


# Player move
def button_click(index):
    if board[index] == "":
        board[index] = player
        buttons[index].config(text=player)

        winner = check_winner()

        if winner:
            if winner == "Tie":
                messagebox.showinfo("Game Over", "It's a Tie!")
            else:
                messagebox.showinfo(
                    "Winner",
                    "Congratulations! You Win!"
                )
            reset_game()
            return

        # Computer turn
        computer_move()


# Restart game
def reset_game():
    global board

    board = [""] * 9

    for button in buttons:
        button.config(text="")


# Title
title_label = Label(
    root,
    text="TIC TAC TOE",
    font=("Arial", 22, "bold"),
    bg="lightblue",
    fg="darkblue"
)

title_label.pack(pady=10)

# Subtitle
subtitle = Label(
    root,
    text="You (X) vs Computer (O)",
    font=("Arial", 14),
    bg="lightblue"
)

subtitle.pack(pady=5)

# Frame for board
frame = Frame(root)
frame.pack(pady=20)

# Create buttons
for i in range(9):
    button = Button(
        frame,
        text="",
        font=("Arial", 25, "bold"),
        width=6,
        height=2,
        command=lambda i=i: button_click(i)
    )

    button.grid(
        row=i // 3,
        column=i % 3,
        padx=5,
        pady=5
    )

    buttons.append(button)

# Restart button
restart_btn = Button(
    root,
    text="Restart Game",
    font=("Arial", 14, "bold"),
    bg="green",
    fg="white",
    command=reset_game
)

restart_btn.pack(pady=20)

# Run app
root.mainloop()