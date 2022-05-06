import time
import os
import csv
import uuid

from SimConnect import *

docs_path = os.path.join(
    os.path.expanduser("~/Documents"),
    "Flight Tracker"
)
output_file_path = os.path.join(docs_path, f"{str(uuid.uuid4())}.csv")

print(f"beginning flight tracking, output file is {output_file_path}")

sm = SimConnect()
two_seconds = 2000
aq = AircraftRequests(sm, _time=two_seconds)

try:
    os.mkdir(docs_path)
except FileExistsError:
    pass

altitude = aq.find("PLANE_ALTITUDE")

with open(output_file_path, "w", newline="") as f:
    fieldnames = ["altitude"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

while True:
    with open(output_file_path, "a", newline="") as f:
        fieldnames = ["altitude"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({"altitude": str(altitude.get())})

    time.sleep(3)