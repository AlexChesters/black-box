install:
	poetry install

run:
	poetry run python -m main

test:
	poetry run pylint flight_tracker flight_tracker.py

clean:
	rm -rf build
	rm -rf dist

build: clean test
	poetry run pyinstaller -c -F --add-binary "./SimConnect.dll:." flight_tracker.py