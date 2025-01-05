import random
import tkinter as tk
from tkinter import messagebox

# Function to start a new game
def start_new_game():
    global secret_number
    secret_number = random.randint(1, 20)
    guess_entry.delete(0, tk.END)
    info_label.config(text="🤔 I'm thinking of a number between 1 and 20.\nCan you guess it?")

# Function to check the user's guess
def check_guess():
    guess = guess_entry.get().strip().lower()

    if guess == 'x':
        root.destroy()
    elif guess == 's':
        messagebox.showinfo("🔍 Secret Number", f"👀 The secret number is: {secret_number}")
    elif not guess.isdigit():
        messagebox.showwarning("⚠️ Invalid Input", "⛔ Please enter a valid number between 1 and 20!")
    else:
        guess = int(guess)
        if guess < 1 or guess > 20:
            messagebox.showwarning("⚠️ Out of Range", "⛔ Your guess must be between 1 and 20!")
        elif guess < secret_number:
            info_label.config(text="📉 Too small! Try a bigger number.")
        elif guess > secret_number:
            info_label.config(text="📈 Too big! Try a smaller number.")
        else:
            if messagebox.askyesno("🎉 Victory!", "🥳 Congratulations! You guessed it! Play again?"):
                start_new_game()
            else:
                root.destroy()

# Function to reveal the secret number
def reveal_hidden_number():
    messagebox.showinfo("🔍 Secret Number", f"👀 The secret number is: {secret_number}")

# Create the GUI window
root = tk.Tk()
root.title("🎲 Number Guessing Game 🎲")
root.geometry("450x400")
root.configure(bg="#F5F5F5")

# Generate the secret number
secret_number = random.randint(1, 20)

# Create and style GUI widgets
info_label = tk.Label(root, text="🤔 I'm thinking of a number between 1 and 20.\nCan you guess it?", font=("Helvetica", 14), bg="#F5F5F5", fg="#333")
info_label.pack(pady=20)

guess_entry = tk.Entry(root, font=("Helvetica", 14), justify="center")
guess_entry.pack(pady=10)

check_button = tk.Button(root, text="🔍 Check Guess", command=check_guess, font=("Helvetica", 12), bg="#007BFF", fg="white", relief="groove")
check_button.pack(pady=5)

reveal_button = tk.Button(root, text="👀 Reveal Secret Number", command=reveal_hidden_number, font=("Helvetica", 12), bg="#28A745", fg="white", relief="groove")
reveal_button.pack(pady=5)

new_game_button = tk.Button(root, text="🎮 New Game", command=start_new_game, font=("Helvetica", 12), bg="#FFC107", fg="black", relief="groove")
new_game_button.pack(pady=5)

exit_button = tk.Button(root, text="❌ Exit", command=root.destroy, font=("Helvetica", 12), bg="#DC3545", fg="white", relief="groove")
exit_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
