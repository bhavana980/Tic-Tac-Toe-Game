from tkinter import *
from tkinter import messagebox

# Create main window
root = Tk()
root.title("Tic Tac Toe")
root.geometry("400x500")
root.configure(bg="lightblue")

# Variables
current_player = "X"
board = [""] * 9
buttons = []


# Function to check winner
def check_winner():
    winning_positions = [
        [0, 1, 2],  # Row 1
        [3, 4, 5],  # Row 2
        [6, 7, 8],  # Row 3
        [0, 3, 6],  # Column 1
        [1, 4, 7],  # Column 2
        [2, 5, 8],  # Column 3
        [0, 4, 8],  # Diagonal
        [2, 4, 6]   # Diagonal
    ]

    for combo in winning_positions:
        a, b, c = combo

        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]

    if "" not in board:
        return "Tie"

    return None


# Function when player clicks button
def button_click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)

        winner = check_winner()

        if winner:
            if winner == "Tie":
                messagebox.showinfo("Game Over", "It's a Tie!")
            else:
                messagebox.showinfo(
                    "Winner",
                    f"Congratulations! Player {winner} Wins!"
                )

            reset_game()
            return

        # Change player turn
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

        status_label.config(
            text=f"Player {current_player}'s Turn"
        )


# Function to reset game
def reset_game():
    global current_player, board

    current_player = "X"
    board = [""] * 9

    for button in buttons:
        button.config(text="")

    status_label.config(
        text="Player X's Turn"
    )


# Title Label
title_label = Label(
    root,
    text="TIC TAC TOE GAME",
    font=("Arial", 22, "bold"),
    bg="lightblue",
    fg="darkblue"
)
title_label.pack(pady=15)


# Status Label
status_label = Label(
    root,
    text="Player X's Turn",
    font=("Arial", 15, "bold"),
    bg="lightblue",
    fg="black"
)
status_label.pack(pady=10)


# Frame for game board
frame = Frame(root, bg="lightblue")
frame.pack()


# Create buttons (3x3 grid)
for i in range(9):
    button = Button(
        frame,
        text="",
        font=("Arial", 25, "bold"),
        width=6,
        height=2,
        bg="white",
        fg="black",
        command=lambda i=i: button_click(i)
    )

    button.grid(
        row=i // 3,
        column=i % 3,
        padx=5,
        pady=5
    )

    buttons.append(button)


# Restart Button
restart_button = Button(
    root,
    text="Restart Game",
    font=("Arial", 14, "bold"),
    bg="green",
    fg="white",
    command=reset_game
)

restart_button.pack(pady=20)


# Run the window
root.mainloop()