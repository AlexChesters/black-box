import datetime
import math
from dataclasses import dataclass

from numpy.testing import assert_almost_equal
import SimConnect

from ..utils.env import is_development_environment

class SimulatorConnectionError(Exception):
    pass

class SimulatorNotInFlightError(Exception):
    pass

@dataclass
class BlackBox:
    fieldnames = [
        "timestamp",
        "aircraft",
        "altitude",
        "latitude",
        "longitude",
        "ground_speed",
        "heading",
        "on_ground",
        "fuel"
    ]

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

    def raise_if_not_in_flight(self):
        latitude = float(self.aircraft_requests.find("PLANE_LATITUDE").get())
        longitude = float(self.aircraft_requests.find("PLANE_LONGITUDE").get())
        on_ground = int(self.aircraft_requests.find("SIM_ON_GROUND").get())

        # msfs says you are at these coordinates when not flying (i.e. in the menu)
        # ideally there'd be a SimVar like IN_AIRCRAFT but...
        try:
            assert_almost_equal(latitude, 0.00040736537119006786)
            assert_almost_equal(longitude, 0.01397450300629543)
            if on_ground:
                raise SimulatorNotInFlightError
        except AssertionError:
            pass

    def get_data(self):
        timestamp = datetime.datetime.now().isoformat()
        aircraft = self.aircraft_requests.find("TITLE")
        altitude = self.aircraft_requests.find("PLANE_ALTITUDE")
        latitude = self.aircraft_requests.find("PLANE_LATITUDE")
        longitude = self.aircraft_requests.find("PLANE_LONGITUDE")
        ground_speed = self.aircraft_requests.find("GROUND_VELOCITY")
        heading = self.aircraft_requests.find("PLANE_HEADING_DEGREES_TRUE")
        on_ground = self.aircraft_requests.find("SIM_ON_GROUND")
        fuel = self.aircraft_requests.find("FUEL_TOTAL_QUANTITY_WEIGHT")

        self.raise_if_not_in_flight()

        return {
            "timestamp": str(timestamp),
            "aircraft": str(aircraft.get()),
            "altitude": int(altitude.get()),
            "latitude": float(latitude.get()),
            "longitude": float(longitude.get()),
            "ground_speed": int(ground_speed.get()),
            "heading": int(math.degrees(heading.get())),
            "on_ground": int(on_ground.get()),
            # FUEL_TOTAL_QUANTITY_WEIGHT returns lbs, we track kilos
            "fuel": int(int(fuel.get()) / 2.205)
        }
