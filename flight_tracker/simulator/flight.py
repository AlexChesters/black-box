import math
from re import M

import SimConnect

from ..utils.env import is_development_environment

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
            "timestamp",
            "altitude",
            "latitude",
            "longitude",
            "ground_speed",
            "heading",
            "on_ground",
            "fuel"
        ]

    def get_data(self):
        altitude = self.aircraft_requests.find("PLANE_ALTITUDE")
        latitude = self.aircraft_requests.find("PLANE_LATITUDE")
        longitude = self.aircraft_requests.find("PLANE_LONGITUDE")
        ground_speed = self.aircraft_requests.find("GROUND_VELOCITY")
        heading = self.aircraft_requests.find("PLANE_HEADING_DEGREES_TRUE")
        on_ground = self.aircraft_requests.find("SIM_ON_GROUND")
        fuel = self.aircraft_requests.find("FUEL_TOTAL_QUANTITY_WEIGHT")

        return {
            "altitude": int(altitude.get()),
            "latitude": float(latitude.get()),
            "longitude": float(longitude.get()),
            "ground_speed": int(ground_speed.get()),
            "heading": int(math.degrees(heading.get())),
            "on_ground": int(on_ground.get()),
            "fuel": int(int(fuel.get()) / 2.205)
        }
