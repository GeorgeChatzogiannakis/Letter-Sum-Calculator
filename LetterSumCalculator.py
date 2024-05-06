import tkinter as tk
import re

def count_words(text_content):
    words = re.findall(r'\b\w+\b', text_content)
    return len(words)

def count_letters(text_content):
    text_without_whitespace = text_content.replace(" ", "")  
    return len(text_without_whitespace)

def count_whitespace(text_content):
    return text_content.count(' ')

def update_counts(event=None):
    text_content = text.get("1.0", "end-1c")  # Get text from the text widget
    words_count = count_words(text_content)  # Count words
    letters_count = count_letters(text_content)  # Count letters without counting white spaces
    whitespace_count = count_whitespace(text_content)  # Count white spaces
    words.config(text="Words: " + str(words_count))  # Update the words label
    letters.config(text="Letters: " + str(letters_count))  # Update the letters label
    whitespace_label.config(text="White Spaces: " + str(whitespace_count))  # Update the white spaces label
    if whitespace_var.get() == True:
        whitespace_label.pack(pady=5)
    else:
        whitespace_label.pack_forget()

root = tk.Tk()
root.title("Letter Sum Calculator")
root.geometry("400x500")

frame = tk.Frame(root)
frame.pack()

title = tk.Label(frame, text="Letter Sum Calculator")
title.pack(pady=10)

text = tk.Text(frame, width=45, height=20)
text.config(wrap="word")
text.pack()
text.bind("<KeyRelease>", update_counts)  # Bind the update_counts function to KeyRelease event

words = tk.Label(frame, text="Words: 0")
words.pack(side="left", pady=5)

letters = tk.Label(frame, text="Letters: 0")
letters.pack(side="right", pady=5)

whitespace_var = tk.BooleanVar()
whitespace_checkbox = tk.Checkbutton(frame, text="Count white spaces", variable=whitespace_var, command=update_counts)
whitespace_checkbox.pack(pady=5)

whitespaces = tk.Frame(root)
whitespaces.pack()

whitespace_label = tk.Label(whitespaces, text="White Spaces: 0")

root.mainloop()
