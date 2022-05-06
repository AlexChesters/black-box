import time
import sys

from .utils.logger import Logger
from .utils.env import is_development_environment
from .results.results_writer import ResultsWriter
from .simulator.flight import Flight, SimulatorConnectionError

def main():
    logger = Logger()

    try:
        flight = Flight()
    except SimulatorConnectionError:
        logger.error("Could not connect to Flight Simulator. Verify the simulator is running.")
        sys.exit(1)

    results_writer = ResultsWriter(flight.fieldnames)

    logger.log(f"beginning flight tracking, output file is {results_writer.output_file_path}")

    while True:
        logger.log("appending record")
        results_writer.append_record(flight.get_data())
        time.sleep(3 if is_development_environment() else 30)
