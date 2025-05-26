import tkinter as tk
from tkinter import messagebox
import math

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def evaluate(event=None):  # Se agrega event para que funcione con Enter
    try:
        result = eval(entry.get(), {"__builtins__": None}, math.__dict__)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", f"Entrada inválida\n{e}")

def move_cursor_up():
    entry.icursor(entry.index(tk.INSERT) - 1)

def move_cursor_down():
    entry.icursor(entry.index(tk.INSERT) + 1)

root = tk.Tk()
root.title("ELBARNY - Calculadora Científica")

# Pantalla de la calculadora
frame = tk.Frame(root, bd=5, relief=tk.SUNKEN, bg="black")
frame.pack(pady=10)
label = tk.Label(frame, text="ELBARNY", font=("Arial", 18, "bold"), fg="white", bg="black")
label.pack()
entry = tk.Entry(frame, width=30, font=("Arial", 16), bd=5, relief=tk.SUNKEN)
entry.pack()
entry.bind("<Return>", evaluate)  # Permite calcular usando Enter

# Botones organizados en filas
buttons = [
    ('7', '8', '9', '/', 'C'),
    ('4', '5', '6', '*', '√'),
    ('1', '2', '3', '-', 'log'),
    ('0', '.', '+', '=', 'exp'),
    ('sin', 'cos', 'tan', '^', 'pow'),
    ('↑', '↓')  # Botones de navegación
]

frame_buttons = tk.Frame(root)
frame_buttons.pack()

for i, row in enumerate(buttons):
    for j, char in enumerate(row):
        if char == "=":
            button = tk.Button(frame_buttons, text=char, width=5, height=2, command=evaluate)
        elif char == "C":
            button = tk.Button(frame_buttons, text=char, width=5, height=2, command=clear)
        elif char == "√":
            button = tk.Button(frame_buttons, text=char, width=5, height=2, command=lambda: press("math.sqrt("))
        elif char == "log":
            button = tk.Button(frame_buttons, text=char, width=5, height=2, command=lambda: press("math.log("))
        elif char == "exp":
            button = tk.Button(frame_buttons, text=char, width=5, height=2, command=lambda: press("math.exp("))
        elif char == "^":
            button = tk.Button(frame_buttons, text=char, width=5, height=2, command=lambda: press("**"))
        elif char == "pow":
            button = tk.Button(frame_buttons, text=char, width=5, height=2, command=lambda: press("math.pow("))
        elif char in ("sin", "cos", "tan"):
            button = tk.Button(frame_buttons, text=char, width=5, height=2, command=lambda c=char: press(f"math.{c}("))
        elif char == "↑":
            button = tk.Button(frame_buttons, text=char, width=5, height=2, command=move_cursor_up)
        elif char == "↓":
            button = tk.Button(frame_buttons, text=char, width=5, height=2, command=move_cursor_down)
        else:
            button = tk.Button(frame_buttons, text=char, width=5, height=2, command=lambda c=char: press(c))
        
        button.grid(row=i, column=j)

root.mainloop()