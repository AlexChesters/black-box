# black box
record data about your [MSFS](https://www.flightsimulator.com/) flights

# what does it do?
outputs information from a current MSFS flight to a CSV file in `~/Documents/Black Box`

# can I use it?
if you have the PC version of MSFS then yes (although be aware that currently this program is very much a work-in-progress and the executable isn't signed)

1. download the [executable](https://projects.alexchesters.com/black-box/Black%20Box.exe)
1. place the executable wherever you'd like (it doesn't need to be on the same drive that MSFS is installed on, but it does need to be on the same PC)
1. run `Black Box.exe` once you've spawned into your aircraft

# development instructions

## dependencies
* `poetry` - 1.1.13
* `python` - 3.10.0

everything else should (hopefully) be obvious from the `Makefile`
