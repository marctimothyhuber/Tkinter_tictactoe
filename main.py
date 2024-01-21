import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Tkinter TicTacToe by Heimatbrot")

# Header
label = tk.Label(window, text="Tkinter Tic Tac Toe")
label.grid(row=0, column=0, columnspan=3)

# Grid definition and played steps
grid = [["", "", ""], ["", "", ""], ["", "", ""]]
played = [["", "", ""], ["", "", ""], ["", "", ""]]

# Create buttons
def create_grid():
    global grid
    for i in range(3):
        for j in range(3):
            grid[i][j] = tk.Button(window, height=4, width=6, command=lambda row=i, col=j: on_button_click(row, col))
            grid[i][j].grid(row=i + 1, column=j, padx=5, pady=5)  # Increase the row index
    return

# Next turn
turn = "X"
# Function to handle button click
def on_button_click(row, col):
    global turn
    global played
    label_text = {"X": "O", "O": "X"}

    grid[row][col].configure(text=turn)
    grid[row][col].configure(state="disabled")
    played[row][col] = turn
    checkwinner()
    turn = label_text[turn]
    return

# Check winner function
def checkwinner():
    global played
    for row in played: 
        if row[0] == row[1] == row[2] != "":
            return winner(row[0])
    for col in range(3):
        if played[0][col] == played[1][col] == played[2][col] != "":
            return winner(played[0][col])
    if played[0][0] == played[1][1] == played[2][2] != "":
        return winner(played[0][0])
    elif played[0][2] == played[1][1] == played[2][0] != "":
        return winner(played[0][2]) 

# Communicate winner
def winner(winner):
    label2 = tk.Label(window, text="The winner is " + winner)
    label2.grid(row=5, column=0, columnspan=3)
    return destroygrid()

# Destroy grid when winner is found
def destroygrid():
    global grid
    for i in range(3):
        for j in range(3):
            if played[i][j] == "":
                grid[i][j].configure(text="-")
                grid[i][j].configure(state="disabled")
    return

# Call the create_grid function to initialize the grid
create_grid()

# Start the main event loop
if __name__ == "__main__":
    window.mainloop()
