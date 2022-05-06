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

    tkinter.Label(
        window,
        text=f"Beginning flight tracking, output file is {results_writer.output_file_path}"
    ).grid(column=0, row=0)

    def process():
        results_writer.append_record(flight.get_data())
        tkinter.Label(
            window,
            text=f"Data last written at {datetime.datetime.now().isoformat()}"
        ).grid(column=0, row=1)
        window.after(3000 if is_development_environment() else 30000, process)

    window.after(0, process)

    window.mainloop()
