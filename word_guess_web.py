import random
import tkinter as tk
from tkinter import messagebox

# Endless word list
word_list = ["python", "github", "developer", "programming", "computer", 
             "algorithm", "software", "hardware", "keyboard", "monitor",
             "mouse", "function", "variable", "database", "network"]

# Function to reset the game with a new word
def new_game():
    global word, guessed_word, attempts, guessed_letters
    word = random.choice(word_list)
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()
    update_display()

# Function to update the GUI
def update_display():
    word_label.config(text=" ".join(guessed_word))
    hearts_label.config(text="❤️" * attempts)  # Show hearts instead of numbers
    entry.delete(0, tk.END)  # Clear the input box

# Function to process guesses
def guess_letter():
    global attempts
    letter = entry.get().lower()

    if len(letter) != 1 or not letter.isalpha():
        messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        return

    if letter in guessed_letters:
        messagebox.showwarning("Duplicate", "You already guessed that letter!")
        return

    guessed_letters.add(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed_word[i] = letter
    else:
        attempts -= 1

    update_display()

    if "_" not in guessed_word:
        messagebox.showinfo("Congratulations", f"You guessed the word: {word}")
        new_game()  # Start a new game
    elif attempts == 0:
        messagebox.showerror("Game Over", f"You lost! The word was: {word}")
        new_game()  # Start a new game

# GUI Setup
root = tk.Tk()
root.title("Word Guessing Game")

tk.Label(root, text="Guess the word:", font=("Arial", 14)).pack()
word_label = tk.Label(root, text="", font=("Arial", 16))
word_label.pack()

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

tk.Button(root, text="Guess", command=guess_letter, font=("Arial", 14)).pack()

hearts_label = tk.Label(root, text="", font=("Arial", 16), fg="red")
hearts_label.pack()

# Start the first game
new_game()

root.mainloop()
