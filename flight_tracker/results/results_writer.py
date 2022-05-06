from operator import delitem
import os
import csv
import uuid
import datetime

# absolute path to the directory name this script lives in
SCRIPT_DIR = os.path.dirname(__file__)

ENVIRONMENT = os.environ.get("ENVIRONMENT", "production")

class ResultsWriter:
    def __init__(self, fieldnames):
        self._fieldnames = fieldnames

        docs_path = os.path.join(
            os.path.expanduser("~/Documents"),
            "Flight Tracker"
        )

        try:
            os.mkdir(docs_path)
        except FileExistsError:
            pass

        if ENVIRONMENT == "development":
            self.output_file_path = os.path.join(SCRIPT_DIR, "../../", "results.csv")
        else:
            self.output_file_path = os.path.join(
                docs_path, f"{str(uuid.uuid4())}.csv"
            )

        with open(self.output_file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self._fieldnames)
            writer.writeheader()

    def append_record(self, record):
        record.update({"timestamp": datetime.datetime.now().isoformat()})

        with open(self.output_file_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self._fieldnames)
            writer.writerow(record)
