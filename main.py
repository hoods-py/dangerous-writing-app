from tkinter import Tk, Text, messagebox
import threading

class WritingApp:

    def __init__(self, master):
        self.master = master
        self.text = Text(master)
        self.text.pack()
        self.reset_timer()

    def reset_timer(self):
        try:
            self.timer.cancel()
        except AttributeError:
            pass

        self.timer = threading.Timer(5.0, self.time_up)  # Change number to amount of seconds
        self.timer.start()

    def text_modified(self, event):
        self.reset_timer()

    def time_up(self):
        self.text.delete('1.0', 'end')
        messagebox.showinfo('Time\'s up', 'You didn\'t write for too long. Your progress has been deleted.')


root = Tk()
app = WritingApp(root)
root.bind('<Key>', app.text_modified)
root.mainloop()