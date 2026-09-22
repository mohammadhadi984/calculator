import tkinter as tk


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def add(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")
window.resizable(False, False)

display = tk.Entry(
    window,
    font=("Arial", 24),
    justify="right"
)
display.pack(
    padx=10,
    pady=20,
    fill="x"
)

buttons = [
    ("7", "7"), ("8", "8"), ("9", "9"), ("/", "/"),
    ("4", "4"), ("5", "5"), ("6", "6"), ("*", "*"),
    ("1", "1"), ("2", "2"), ("3", "3"), ("-", "-"),
    ("0", "0"), (".", "."), ("=", "="), ("+", "+"),
]

frame = tk.Frame(window)
frame.pack()

for i, (text, value) in enumerate(buttons):
    if text == "=":
        command = calculate
    else:
        command = lambda v=value: add(v)

    button = tk.Button(
        frame,
        text=text,
        font=("Arial", 18),
        width=5,
        height=2,
        command=command
    )

    button.grid(
        row=i // 4,
        column=i % 4,
        padx=3,
        pady=3
    )


clear_button = tk.Button(
    window,
    text="CLEAR",
    font=("Arial", 16),
    width=20,
    command=clear
)

clear_button.pack(pady=10)

window.mainloop()