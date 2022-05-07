import time

from .results.results_writer import ResultsWriter
from .simulator.flight import Flight

class FlightTracker:
    def __init__(self, departure, arrival):
        self._flight = Flight(departure, arrival)

        self._results_writer = ResultsWriter(self._flight.fieldnames)
        self.output_file_path = self._results_writer.output_file_path
        self._continue_tracking = True

    def start_tracking(self, on_iteration):
        while self._continue_tracking:
            self._results_writer.append_record(self._flight.get_data())
            on_iteration()
            time.sleep(3)

    def stop_tracking(self):
        self._continue_tracking = False
