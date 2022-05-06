import time

from SimConnect import *

# Create SimConnect link
sm = SimConnect()
# Note the default _time is 2000 to be refreshed every 2 seconds
aq = AircraftRequests(sm, _time=2000)

altitude = aq.find("PLANE_ALTITUDE")

with open("foo.txt", "w") as f:
    f.write(str(altitude.get()))

while True:
    print(altitude.get())
    time.sleep(3)