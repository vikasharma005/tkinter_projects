import tkinter as tk
from tkinter import filedialog

class NoteTakingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note-taking App")

        self.note_text = tk.Text(root, height=10, width=40)
        self.note_text.pack()

        self.save_button = tk.Button(root, text="Save", command=self.save_note)
        self.save_button.pack()

        self.load_button = tk.Button(root, text="Load", command=self.load_note)
        self.load_button.pack()

    def save_note(self):
        note_content = self.note_text.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

        if file_path:
            with open(file_path, "w") as file:
                file.write(note_content)
                print("Note saved successfully.")

    def load_note(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if file_path:
            with open(file_path, "r") as file:
                note_content = file.read()
                self.note_text.delete("1.0", tk.END)
                self.note_text.insert(tk.END, note_content)
                print("Note loaded successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteTakingApp(root)
    root.mainloop()
