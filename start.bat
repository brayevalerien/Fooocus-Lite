@echo off

set "FLPATH=.\"

echo ======== Starting Fooocus Lite ========
echo Activating virtual environement...
CALL conda activate flite

echo Lauching Fooocus Lite...
python %FLPATH%start.py --preset realistic

echo Process got interrupted.
pause