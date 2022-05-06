import time

import SimConnect

from .utils.results_writer import ResultsWriter

results_writer = ResultsWriter()

print(
    f"beginning flight tracking, output file is {results_writer.output_file_path}"
)

sm = SimConnect.SimConnect()
TWO_SECONDS = 2000
aq = SimConnect.AircraftRequests(sm, _time=TWO_SECONDS)

altitude = aq.find("PLANE_ALTITUDE")

while True:
    results_writer.append_record(altitude=str(altitude.get()))
    time.sleep(3)
