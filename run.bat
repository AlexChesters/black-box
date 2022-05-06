ECHO ON
REM A batch script to execute flight-tracker
SET PATH=%PATH%;C:\Python310
poetry run python -m flight_tracker.main.py
PAUSE