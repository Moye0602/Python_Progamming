import tkinter as tk

def say_hello():
    response_label.config(text="Hello!")

# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Add a label
label = tk.Label(root, text="Hello, this is a simple GUI!")
label.pack()

# Add a button
button = tk.Button(root, text="Say Hello", command=say_hello)
button.pack()

# Add a label to display the response
response_label = tk.Label(root, text="")
response_label.pack()

# Run the event loop
root.mainloop()
