import math

import SimConnect

class SimulatorConnectionError(Exception):
    pass

class Flight:
    def __init__(self):
        try:
            sim_connect = SimConnect.SimConnect()
        except ConnectionError as e:
            raise SimulatorConnectionError from e

        five_seconds = 5000

        self.aircraft_requests = SimConnect.AircraftRequests(sim_connect, _time=five_seconds)
        self.fieldnames = [
            "timestamp",
            "altitude",
            "latitude",
            "longitude",
            "ground_speed",
            "heading"
        ]

    def get_data(self):
        altitude = self.aircraft_requests.find("PLANE_ALTITUDE")
        latitude = self.aircraft_requests.find("PLANE_LATITUDE")
        longitude = self.aircraft_requests.find("PLANE_LONGITUDE")
        ground_speed = self.aircraft_requests.find("GROUND_VELOCITY")
        heading = self.aircraft_requests.find("PLANE_HEADING_DEGREES_TRUE")

        return {
            "altitude": int(altitude.get()),
            "latitude": float(latitude.get()),
            "longitude": float(longitude.get()),
            "ground_speed": int(ground_speed.get()),
            "heading": int(math.degrees(heading.get()))
        }
