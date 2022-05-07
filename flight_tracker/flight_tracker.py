from .results.results_writer import ResultsWriter
from .simulator.flight import Flight

class FlightTracker:
    def __init__(self):
        self._flight = Flight()

        self._results_writer = ResultsWriter(self._flight.fieldnames)
        self.output_file_path = self._results_writer.output_file_path

    def track(self):
        self._results_writer.append_record(self._flight.get_data())
