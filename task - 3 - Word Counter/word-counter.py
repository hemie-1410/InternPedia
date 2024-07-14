import tkinter as tk
from tkinter import messagebox
import re

def count_words():
    try:
        text = text_area.get("1.0", tk.END)
        words = re.findall(r'\b\w+\b', text)
        word_count = len(words)
        char_count = len(text)
        result_label.config(text=f"Word count: {word_count}\nCharacter count: {char_count}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_text():
    text_area.delete("1.0", tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Word Counter")

text_area = tk.Text(root, height=10, width=50)
text_area.pack()

button_count_words = tk.Button(root, text="Count words", width=48, command=count_words)
button_count_words.pack()

button_clear_text = tk.Button(root, text="Clear text", width=48, command=clear_text)
button_clear_text.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()