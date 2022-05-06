import datetime
import sys
import tkinter

from .utils.env import is_development_environment
from .results.results_writer import ResultsWriter
from .simulator.flight import Flight, SimulatorConnectionError

def main():
    try:
        flight = Flight()
    except SimulatorConnectionError:
        tkinter.messagebox.showerror(
            "Connection error",
            "Could not connect to Flight Simulator. Verify the simulator is running."
        )
        sys.exit(1)

    results_writer = ResultsWriter(flight.fieldnames)

    window = tkinter.Tk()

    window.title("Flight Tracker")
    window.geometry("800x800")

    top_frame = tkinter.Frame(window)
    top_frame.pack(side="top")

    center_frame = tkinter.Frame(window)
    center_frame.pack(fill="both")

    bottom_frame = tkinter.Frame(window)
    bottom_frame.pack(side="bottom")

    tkinter.Label(
        top_frame,
        text=f"Beginning flight tracking, output file is {results_writer.output_file_path}",
        font=("Arial Bold", 14),
        wraplength=800,
        justify="center"
    ).grid(column=0, row=0)

    def process():
        results_writer.append_record(flight.get_data())
        tkinter.Label(
            bottom_frame,
            text=f"Data last written at {datetime.datetime.now().isoformat()}",
            font=("Arial Bold", 10)
        ).grid(column=0, row=1)
        window.after(3000 if is_development_environment() else 30000, process)

    def start_process():
        window.after(0, process)

    tkinter.Button(
        center_frame,
        text="Start tracking",
        command=start_process
    ).pack()

    window.mainloop()
