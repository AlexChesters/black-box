install:
	poetry install

run:
	ENVIRONMENT=development poetry run python main.py

test:
	poetry run pylint black_box main.py

clean:
	rm -rf build
	rm -rf dist

build: clean test
	poetry run pyinstaller \
		--name "Black Box" \
		--noconsole \
		--onefile \
		--add-binary "./vendor/SimConnect.dll:." \
		--icon "./assets/black_box.ico" \
		main.py
