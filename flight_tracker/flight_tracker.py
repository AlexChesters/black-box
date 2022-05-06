import time
import sys
from tkinter import messagebox

from .utils.env import is_development_environment
from .results.results_writer import ResultsWriter
from .simulator.flight import Flight, SimulatorConnectionError

def main():
    try:
        flight = Flight()
    except SimulatorConnectionError:
        messagebox.showerror(
            "Connection error",
            "Could not connect to Flight Simulator. Verify the simulator is running."
        )
        sys.exit(1)

    results_writer = ResultsWriter(flight.fieldnames)

    while True:
        results_writer.append_record(flight.get_data())
        time.sleep(3 if is_development_environment() else 30)
