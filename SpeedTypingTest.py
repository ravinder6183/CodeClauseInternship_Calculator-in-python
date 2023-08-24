import tkinter as tk
import random
import time


class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.text = "The quick brown fox jumps over the lazy dog"
        self.words = self.text.split()
        self.current_word_index = 0
        self.typing_started = False
        self.start_time = 0

        self.label = tk.Label(self.root, text=self.text)
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16, "bold"))
        self.result_label.pack(pady=20)

        self.time_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.time_label.pack()

        self.start_button = tk.Button(self.root, text="Start Typing Test", command=self.start_typing_test)
        self.start_button.pack()

    def start_typing_test(self):
        if not self.typing_started:
            self.typing_started = True
            self.start_time = time.time()
            self.start_button.config(state=tk.DISABLED)
            self.entry.bind("<KeyRelease>", self.check_input)
            self.update_time()

    def update_time(self):
        if self.typing_started:
            elapsed_time = time.time() - self.start_time
            self.time_label.config(text=f"Time elapsed: {elapsed_time:.2f} seconds")
            self.root.after(100, self.update_time)

    def check_input(self, event):
        typed_text = self.entry.get()
        if typed_text == self.text:
            elapsed_time = time.time() - self.start_time
            words_per_minute = len(self.words) / (elapsed_time / 60)
            self.result_label.config(text=f"Typing speed: {words_per_minute:.2f} words per minute", fg="green")
            self.typing_started = False
            self.entry.unbind("<KeyRelease>")
        else:
            self.entry.delete(len(typed_text), tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
