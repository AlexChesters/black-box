from dataclasses import dataclass

from .results.results_writer import ResultsWriter
from .simulator.black_box import BlackBox

@dataclass
class FlightTracker:
    def __init__(self):
        self._black_box = BlackBox()

        self._results_writer = ResultsWriter(self._black_box.fieldnames)
        self.output_file_path = self._results_writer.output_file_path

    def track(self):
        self._results_writer.append_record(self._black_box.get_data())
