import tkinter as tk
from tkinter import ttk
import random
import string
def generate_password():
    try:
        length = int(length_entry.get())

    except:
        result_label.config(text="Error: Enter a valid length for your password!")

    complexity = complexity_combobox.get()
    if complexity == "Easy":
        use_letters = True
        use_numbers = True
        use_symbols = False
    elif complexity == "Medium":
        use_letters = True
        use_numbers = True
        use_symbols = True
    elif complexity == "Hard":
        use_letters = True
        use_numbers = True
        use_symbols = True

    exclude_chars = exclude_entry.get()

    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    characters = ''.join(c for c in characters if c not in exclude_chars)

    if not characters:
        result_label.config(text="Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=password)

def copy_to_clipboard():
    password = result_label.cget("text")
    
# Create main window
root = tk.Tk()
root.title("Password Generator")
root.resizable(False, False)

# Create input fields and labels
length_label = ttk.Label(root, text="Password Length:", font=('Helvetica', 12))
length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
length_entry = ttk.Entry(root, width=10, font=('Helvetica', 12))
length_entry.grid(row=0, column=1, padx=10, pady=10)

complexity_label = ttk.Label(root, text="Complexity:", font=('Helvetica', 12))
complexity_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
complexity_combobox = ttk.Combobox(root, values=["Easy", "Medium", "Hard"], font=('Helvetica', 12))
complexity_combobox.grid(row=1, column=1, padx=10, pady=10)
complexity_combobox.current(0)

exclude_label = ttk.Label(root, text="Exclude Characters:", font=('Helvetica', 12))
exclude_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
exclude_entry = ttk.Entry(root, width=30, font=('Helvetica', 12))
exclude_entry.grid(row=2, column=1, padx=10, pady=10)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(root, text="", font=('Helvetica', 12))
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()