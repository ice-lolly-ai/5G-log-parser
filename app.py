import tkinter as tk
from tkinter import filedialog, scrolledtext

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Log files", "*.log"), ("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.readlines()
        
        # Display original file content in left window
        left_textbox.delete(1.0, tk.END)
        left_textbox.insert(tk.END, "".join(content))
        
        # Filter and display specific messages in right window with color coding
        right_textbox.delete(1.0, tk.END)
        for line in content:
            if 'fail' in line.lower():
                right_textbox.insert(tk.END, line, 'fail')
            elif 'warning' in line.lower():
                right_textbox.insert(tk.END, line, 'warning')
            elif 'assert' in line.lower():
                right_textbox.insert(tk.END, line, 'assert')

def reset_windows():
    left_textbox.delete(1.0, tk.END)
    right_textbox.delete(1.0, tk.END)

# Create main window
root = tk.Tk()
root.title("Logfile Parser")
root.geometry("800x400")

# Create Reset button in the center above the windows
reset_button = tk.Button(root, text="Reset", command=reset_windows)
reset_button.pack(pady=10)

# Create frames for the two windows (left and right)
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create left window (for original file content)
left_textbox = scrolledtext.ScrolledText(frame, wrap=tk.WORD)
left_textbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
left_textbox.bind("<Button-1>", lambda e: open_file())  # Open file dialog on left window click

# Create right window (for filtered messages with color coding)
right_textbox = scrolledtext.ScrolledText(frame, wrap=tk.WORD)
right_textbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Configure tags for color coding
right_textbox.tag_configure('fail', foreground='red')
right_textbox.tag_configure('warning', foreground='orange')
right_textbox.tag_configure('assert', foreground='blue')
right_textbox.tag_configure('[ERROR  ]', foreground='red')

# Run the Tkinter loop
root.mainloop()
