import math
import datetime
import os

import SimConnect
import yaml

from ..utils.env import is_development_environment

# absolute path to the directory name this script lives in
SCRIPT_DIR = os.path.dirname(__file__)
FLIGHT_DATA_CONFIG_FILE_PATH = os.path.join(SCRIPT_DIR, "flight_data.yml")

class SimulatorConnectionError(Exception):
    pass

class Flight:
    def __init__(self):
        try:
            sim_connect = SimConnect.SimConnect()
        except ConnectionError as e:
            raise SimulatorConnectionError from e

        five_seconds = 5000
        thirty_seconds = 30000

        self.aircraft_requests = SimConnect.AircraftRequests(
            sim_connect,
            _time=five_seconds if is_development_environment() else thirty_seconds
        )

        self.fieldnames = [
            "timestamp"
        ]

        with open(FLIGHT_DATA_CONFIG_FILE_PATH, "r", encoding="utf-8") as f:
            self.flight_data_config = yaml.safe_load(f)

        for entry in self.flight_data_config:
            self.fieldnames.append(entry["name"])

    def get_data(self):
        result = { "timestamp": datetime.datetime.now().isoformat() }

        for entry in self.flight_data_config:
            name = entry["name"]
            var = entry["var"]

            value = self.aircraft_requests.find(var).get()

            match entry["type"]:
                case "integer":
                    result.update({name: int(value)})
                case "float":
                    result.update({name: float(value)})
                case "bool":
                    result.update({name: int(value)})

        return result
