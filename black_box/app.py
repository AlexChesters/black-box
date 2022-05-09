import datetime
from dataclasses import dataclass

import tkinter

from .black_box import BlackBox

@dataclass
class App:
    def __init__(self):
        self._black_box = BlackBox(self.on_data_update)

        self._window = tkinter.Tk()

        self._window.title("Flight Tracker")
        self._window.geometry("800x800")

        top_frame = tkinter.Frame(self._window)
        top_frame.pack(side="top")

        center_frame = tkinter.Frame(self._window, pady=35)
        center_frame.pack()

        bottom_frame = tkinter.Frame(self._window)
        bottom_frame.pack(side="bottom")

        tkinter.Label(
            top_frame,
            text="Flight Tracker",
            font=("Arial Bold", 14),
            wraplength=800,
            justify="center"
        ).grid(column=0, row=0)

        self._last_written_text = tkinter.StringVar()

        def start_process():
            self._window.after(
                0,
                lambda _: self._black_box.track(self._window.after)
            )

        tkinter.Button(
            center_frame,
            text="Start tracking",
            height=1,
            width=20,
            font=("Arial Bold", 12),
            command=start_process
        ).pack()

        tkinter.Label(
            bottom_frame,
            text=f"Output file is {self._black_box.output_file_path}",
            font=("Arial Bold", 10)
        ).grid(column=0, row=1)

        tkinter.Label(
            bottom_frame,
            textvariable=self._last_written_text,
            font=("Arial Bold", 10)
        ).grid(column=0, row=2)

        self._window.mainloop()

    def on_data_update(self):
        last_written_timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        self._last_written_text.set(f"Data last written at {last_written_timestamp}")
