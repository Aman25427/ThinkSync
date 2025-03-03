import tkinter as tk
from tkinter import messagebox
import json
import random
from tkinter import ttk

# Load Questions from JSON File
def load_questions():
    with open('questions.json', 'r') as file:
        return json.load(file)

# Check Answer
def check_answer(selected_option):
    global current_question, score
    if selected_option == questions[current_question]['answer']:
        score += 1
        messagebox.showinfo("Correct!", "You got it right!")
        progress_bar['value'] += (100 / len(questions))
    else:
        messagebox.showerror("Wrong!", "Oops! The correct answer is: " + questions[current_question]['answer'])
    current_question += 1
    if current_question < len(questions):
        display_question()
    else:
        messagebox.showinfo("Quiz Over", f"Your Final Score: {score}/{len(questions)}")
        root.destroy()

# Display Question
def display_question():
    question_label.config(text=questions[current_question]['question'])
    options = questions[current_question]['options']
    random.shuffle(options)
    for i in range(4):
        option_buttons[i].config(text=options[i], command=lambda opt=options[i]: check_answer(opt), bg="#ffcccb", fg="#333333", activebackground="#ffa07a")

# Main Window
root = tk.Tk()
root.title("Quiz Game")
root.geometry("800x600")
root.resizable(False, False)
root.config(bg="#2c3e50")

questions = load_questions()
random.shuffle(questions)
current_question = 0
score = 0

# Title Label
title_label = tk.Label(root, text="QUIZ GAME", font=("Comic Sans MS", 40, "bold"), bg="#2c3e50", fg="#f1c40f")
title_label.pack(pady=20)

# Progress Bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=600, mode="determinate")
progress_bar.pack(pady=10)

# Question Label
question_label = tk.Label(root, text="", font=("Comic Sans MS", 20, "bold"), wraplength=700, justify="center", bg="#2c3e50", fg="#ecf0f1")
question_label.pack(pady=20)

# Option Buttons
option_buttons = [tk.Button(root, text="", font=("Comic Sans MS", 14), width=40, height=2, bd=3, relief="raised", cursor="hand2", bg="#ffcccb") for _ in range(4)]
for button in option_buttons:
    button.pack(pady=5, padx=20, fill="x")
    button.bind("<Enter>", lambda e, btn=button: btn.config(bg="#ffa07a"))
    button.bind("<Leave>", lambda e, btn=button: btn.config(bg="#ffcccb"))

# Footer Label
footer_label = tk.Label(root, text="All the Best!", font=("Comic Sans MS", 16, "italic"), bg="#2c3e50", fg="#f1c40f")
footer_label.pack(pady=20)

display_question()
root.mainloop()
