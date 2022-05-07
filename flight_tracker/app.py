import datetime

import tkinter

from .flight_tracker import FlightTracker

def main():
    window = tkinter.Tk()

    window.title("Flight Tracker")
    window.geometry("800x800")

    top_frame = tkinter.Frame(window)
    top_frame.pack(side="top")

    center_frame = tkinter.Frame(window, pady=35)
    center_frame.pack()

    bottom_frame = tkinter.Frame(window)
    bottom_frame.pack(side="bottom")

    departure = tkinter.StringVar()
    arrival = tkinter.StringVar()

    tkinter.Label(
        top_frame,
        text="Flight Tracker",
        font=("Arial Bold", 14),
        wraplength=800,
        justify="center"
    ).grid(column=0, row=0)

    def update():
        window.update()

    def process():
        tracker = FlightTracker(departure.get(), arrival.get())
        tracker.start_tracking(on_iteration=update)

    def start_process():
        window.after(0, process)

    tkinter.Label(
        bottom_frame,
        text=f"Data last written at {datetime.datetime.now().isoformat()}",
        font=("Arial Bold", 10)
    ).grid(column=0, row=1)

    tkinter.Label(
        center_frame,
        text="Departure ICAO",
        font=("Arial Bold", 12)
    ).pack()
    tkinter.Entry(center_frame, textvariable=departure, font=("Arial Bold", 10)).pack()
    tkinter.Label(
        center_frame,
        text="Arrival ICAO",
        font=("Arial Bold", 12)
    ).pack()
    tkinter.Entry(center_frame, textvariable=arrival, font=("Arial Bold", 10)).pack(pady=10)

    tkinter.Button(
        center_frame,
        text="Start tracking",
        height=1,
        width=20,
        font=("Arial Bold", 12),
        command=start_process
    ).pack()

    window.mainloop()
