import tkinter as tk
from tkinter import messagebox
# Window
root = tk.Tk()

def msg_box():
    messagebox.showinfo("Hello", "This is tkinter's message box example. pretty cool right?")

my_menu = Menu(root)

ex_menu = menu(my_menu, tearoff=0)
my_menu.add_cascade(Label = "Example Menu Bar", menu=ex_menu)
set_menu.add_command(label="Exit", command=root.quit)


root.geometry("500x500")
root.title("example")

label = tk.Label(root, text="example", font=('Comic Sans', 20))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=10, font=('Comic Sans', 16))
textbox.pack(padx=10, pady=10)

button = tk.Button(root, text="Click me!", font=('Arial', 18))
button.pack(padx=10, pady=10)

button = tk.Button(root, text="Msg box example", font=('Arial', 18), command=msg_box)
button.pack(padx=10, pady=10)

root.mainloop()

