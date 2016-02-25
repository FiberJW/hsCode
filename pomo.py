import tkinter
from tkinter import messagebox

DEFAULT_GAP = 60 * 25



class Pymodoro:
    def __init__(self, master):
        self.master = master
        self.mainframe = tkinter.Frame(self.master, bg='white')
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)

        self.timer_text = tkinter.StringVar()
        self.timer_text.trace('w', self.build_timer)
        self.time_left = tkinter.IntVar()
        self.time_left.set(DEFAULT_GAP)
        self.time_left.trace('w', self.alert)
        self.running = False

        self.build_grid()
        self.build_banner()
        self.build_buttons()
        self.build_timer()

        self.update()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=0)

    def build_banner(self):
        banner = tkinter.Label(
            self.mainframe,
            background='red',
            text='Pomodoro',
            fg='white',
            font=('Helvetica', 24)
        )
        banner.grid(
            row=0, column=0,
            sticky='ew',
            padx=10, pady=10
        )

    def build_buttons(self):
        buttons_frame = tkinter.Frame(self.mainframe)
        buttons_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        self.start_button = tkinter.Button(
            buttons_frame,
            text='Start',
            command=self.start_timer
        )
        self.stop_button = tkinter.Button(
            buttons_frame,
            text='Stop',
            command=self.stop_timer
        )
        self.start_button.grid(row=0, column=0, sticky='ew')
        self.stop_button.grid(row=0, column=1, sticky='ew')
        self.stop_button.config(state=tkinter.DISABLED)

    def build_timer(self, *args):
        timer = tkinter.Label(
            self.mainframe,
            text=self.timer_text.get(),
            font=('Helvetica', 36)
        )
        timer.grid(row=1, column=0, sticky='nsew')

    def start_timer(self):
        self.time_left.set(DEFAULT_GAP)
        self.running = True
        self.stop_button.config(state=tkinter.NORMAL)
        self.start_button.config(state=tkinter.DISABLED)

    def stop_timer(self):
        self.running = False
        self.stop_button.config(state=tkinter.DISABLED)
        self.start_button.config(state=tkinter.NORMAL)

    def alert(self, *args):
        if not self.time_left.get():
            messagebox.showinfo('Timer done!', 'Your timer is done!')

    def minutes_seconds(self, seconds):
        return int(seconds/60), int(seconds%60)

    def update(self):
        time_left = self.time_left.get()

        if self.running and time_left:
            minutes, seconds = self.minutes_seconds(time_left)
            self.timer_text.set(
                '{:0>2}:{:0>2}'.format(minutes, seconds)
            )
            self.time_left.set(time_left-1)
        else:
            minutes, seconds = self.minutes_seconds(DEFAULT_GAP)
            self.timer_text.set(
                '{:0>2}:{:0>2}'.format(minutes, seconds)
            )
            self.stop_timer()
        self.master.after(1000, self.update)

if __name__ == '__main__':
    root = tkinter.Tk()
    Pymodoro(root)
    root.mainloop()
