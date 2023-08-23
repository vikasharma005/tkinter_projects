import tkinter as tk
from tkinter import messagebox

class LanguageFlashcardsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Flashcards App")

        self.flashcards = []
        self.current_flashcard_index = 0

        self.word_label = tk.Label(root, text="Word:")
        self.word_label.pack()

        self.word_entry = tk.Entry(root)
        self.word_entry.pack()

        self.translation_label = tk.Label(root, text="Translation:")
        self.translation_label.pack()

        self.translation_entry = tk.Entry(root)
        self.translation_entry.pack()

        self.add_flashcard_button = tk.Button(root, text="Add Flashcard", command=self.add_flashcard)
        self.add_flashcard_button.pack()

        self.next_flashcard_button = tk.Button(root, text="Next Flashcard", command=self.next_flashcard)
        self.next_flashcard_button.pack()

        self.show_translation_button = tk.Button(root, text="Show Translation", command=self.show_translation)
        self.show_translation_button.pack()

    def add_flashcard(self):
        word = self.word_entry.get()
        translation = self.translation_entry.get()
        if word and translation:
            flashcard = (word, translation)
            self.flashcards.append(flashcard)
            self.word_entry.delete(0, tk.END)
            self.translation_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter both word and translation.")

    def next_flashcard(self):
        if self.flashcards:
            self.current_flashcard_index = (self.current_flashcard_index + 1) % len(self.flashcards)
            self.word_label.config(text="Word:")
            self.translation_label.config(text="Translation:")

    def show_translation(self):
        if self.flashcards:
            word, translation = self.flashcards[self.current_flashcard_index]
            self.word_label.config(text=f"Word: {word}")
            self.translation_label.config(text=f"Translation: {translation}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageFlashcardsApp(root)
    root.mainloop()
