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
	poetry run pyinstaller --name flight_tracker --console --onefile --add-binary "./SimConnect.dll:." main.py
