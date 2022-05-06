install:
	poetry install

run:
	ENVIRONMENT=development poetry run python -m main

test:
	poetry run pylint flight_tracker main.py

clean:
	rm -rf build
	rm -rf dist

build: clean test
	poetry run pyinstaller \
		--name "Flight Tracker" \
		--noconsole \
		--onefile \
		--add-binary "./vendor/SimConnect.dll:." \
		--icon "./assets/flight_tracker.ico" \
		main.py
