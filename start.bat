@echo off

set "FLPATH=."
set "NAME=Fooocus Lite"
set "VERSION=1.2"
set "ARGS="

echo ======== Starting Fooocus Lite ========
echo [%NAME% launcher] Activating virtual environment...
call conda activate flite

echo [%NAME% launcher] Lauching Fooocus Lite...
python %FLPATH%/start.py --preset realistic --tab_title "%NAME% v%VERSION%" %ARGS%

echo [%NAME% launcher] Process got interrupted.
pause
