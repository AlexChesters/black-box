from dataclasses import dataclass

from .results.results_writer import ResultsWriter
from .simulator.flight import Flight
from .utils.env import is_development_environment

@dataclass
class BlackBox:
    def __init__(self, on_update):
        self._flight = Flight()
        self._on_update = on_update

        self._results_writer = ResultsWriter(self._flight.fieldnames)
        self.output_file_path = self._results_writer.output_file_path

    def track(self, after):
        self._results_writer.append_record(self._flight.get_data())
        self._on_update()
        after(3000 if is_development_environment() else 30000, self.track)
