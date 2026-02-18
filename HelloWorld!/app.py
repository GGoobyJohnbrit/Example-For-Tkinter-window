
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Window
root = tk.Tk()
root.geometry("500x500")
root.title("Tkinter Example")

# Tabs (for tabs you need ttk)
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# Create tab frames
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text="Home")
notebook.add(tab2, text="Settings")


tk.Label(tab1, text="Welcome to Home tab!", font=('Arial', 16)).pack(pady=20)
tk.Button(tab1, text="Tab 1 Button").pack(pady=10)

tk.Label(tab2, text="Settings go here.", font=('Arial', 16)).pack(pady=20)
tk.Checkbutton(tab2, text="Enable feature").pack(pady=5)
tk.Radiobutton(tab2, text="Option 1", value=1).pack(pady=5)
tk.Radiobutton(tab2, text="Option 2", value=2).pack(pady=5)

# Function for message box
def msg_box():
    messagebox.showinfo("Hello", "This is tkinter's message box example. Pretty cool, right?")

# Menu
my_menu = tk.Menu(root)

ex_menu = tk.Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Example Menu Bar", menu=ex_menu)
ex_menu.add_command(label="Exit", command=root.quit)

root.config(menu=my_menu)  # attach menu to root

# Label
label = tk.Label(root, text="Example", font=('Comic Sans MS', 20))
label.pack(padx=20, pady=20)

# Textbox
textbox = tk.Text(root, height=10, font=('Comic Sans MS', 16))
textbox.pack(padx=10, pady=10)

# Buttons
btn_click = tk.Button(root, text="Click me!", font=('Arial', 18))
btn_click.pack(padx=10, pady=10)

btn_msg = tk.Button(root, text="Msg box example", font=('Arial', 18), command=msg_box)
btn_msg.pack(padx=10, pady=10)

root.mainloop()
