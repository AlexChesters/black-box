ECHO ON
REM A batch script to execute flight-tracker
SET PATH=%PATH%;C:\Python310
SETLOCAL
poetry run python -m main
ENDLOCAL
PAUSE
