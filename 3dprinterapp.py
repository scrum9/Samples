import tkinter as tk
from tkinter import ttk

def calculate_cost():
    material_cost = 0
    if material_var.get() == "PLA":
        material_cost = float(length_entry.get()) * 0.06
    elif material_var.get() == "ABS":
        material_cost = float(length_entry.get()) * 0.12
    elif material_var.get() == "PTEG":
        material_cost = float(length_entry.get()) * 0.07

    hours_cost = float(hours_entry.get()) * 1.50
    total_cost = material_cost + hours_cost

    result_label.config(text=f"Total Cost: ${total_cost:.2f}")

app = tk.Tk()
app.title("3D Printing Cost Calculator")
app.geometry("500x270")  


material_label = tk.Label(app, text="Material Used:")
material_label.pack(pady=5)  

material_var = tk.StringVar()
material_combobox = ttk.Combobox(app, textvariable=material_var, values=["PLA", "ABS", "PTEG"])
material_combobox.pack(pady=5) 

length_label = tk.Label(app, text="Total Length (meters):")
length_label.pack(pady=5)  

length_entry = tk.Entry(app)
length_entry.pack(pady=5)

hours_label = tk.Label(app, text="Hours to Print:")
hours_label.pack(pady=5) 

hours_entry = tk.Entry(app)
hours_entry.pack(pady=5)  


calculate_button = tk.Button(app, text="Calculate Cost", command=calculate_cost)
calculate_button.pack(pady=10)  


result_label = tk.Label(app, text="", font=("Helvetica", 16, "bold"))
result_label.pack(pady=10)  

app.mainloop()
