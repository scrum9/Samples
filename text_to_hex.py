import tkinter as tk
from tkinter import messagebox

def text_to_hex():
    text = text_entry.get()
    if text:
        hex_output = text.encode("utf-8").hex()
        hex_result.set(hex_output)
    else:
        messagebox.showwarning("Warning", "Please enter text.")

def hex_to_text():
    hex_input = hex_entry.get()
    try:
        text_output = bytes.fromhex(hex_input).decode("utf-8")
        text_result.set(text_output)
    except ValueError:
        messagebox.showerror("Error", "Invalid hexadecimal input.")

# Create main window
root = tk.Tk()
root.title("Text to Hex Converter")
root.geometry("400x300")
root.resizable(False, False)

# Labels
tk.Label(root, text="Enter Text:").pack(pady=5)
text_entry = tk.Entry(root, width=40)
text_entry.pack(pady=5)

# Convert to Hex Button
tk.Button(root, text="Convert to Hex", command=text_to_hex).pack(pady=5)

# Hexadecimal Output
hex_result = tk.StringVar()
tk.Entry(root, textvariable=hex_result, width=40, state="readonly").pack(pady=5)

# Labels for Hex input
tk.Label(root, text="Enter Hex:").pack(pady=5)
hex_entry = tk.Entry(root, width=40)
hex_entry.pack(pady=5)

# Convert Hex to Text Button
tk.Button(root, text="Convert to Text", command=hex_to_text).pack(pady=5)

# Text Output
text_result = tk.StringVar()
tk.Entry(root, textvariable=text_result, width=40, state="readonly").pack(pady=5)

# Run the GUI
root.mainloop()
