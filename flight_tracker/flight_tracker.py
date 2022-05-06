import time
import sys

import SimConnect

from .utils.logger import Logger
from .utils.results_writer import ResultsWriter

def main():
    logger = Logger()

    try:
        sm = SimConnect.SimConnect()
    except ConnectionError:
        logger.error("Could not connect to Flight Simulator. Verify the simulator is running.")
        sys.exit(1)

    results_writer = ResultsWriter()

    logger.log(f"beginning flight tracking, output file is {results_writer.output_file_path}")

    five_seconds = 5000
    aq = SimConnect.AircraftRequests(sm, _time=five_seconds)

    altitude = aq.find("PLANE_ALTITUDE")
    latitude = aq.find("PLANE_LATITUDE")
    longitude = aq.find("PLANE_LONGITUDE")

    while True:
        logger.log("appending record")
        results_writer.append_record(
            altitude=str(altitude.get()),
            latitude=float(latitude.get()),
            longitude=float(longitude.get())
        )
        time.sleep(3)
