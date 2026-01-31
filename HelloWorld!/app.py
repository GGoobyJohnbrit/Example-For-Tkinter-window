import tkinter as tk

# Window
root = tk.Tk()

root.geometry("500x500")
root.title("example")

label = tk.Label(root, text="example", font=('Comic Sans', 20))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=10, font=('Comic Sans', 16))
textbox.pack(padx=10, pady=10)

button = tk.Button(root, text="Click me!", font=('Arial', 18))
button.pack(padx=10, pady=10)

root.mainloop()
