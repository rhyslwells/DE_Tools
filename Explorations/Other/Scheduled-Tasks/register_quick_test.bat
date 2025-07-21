@echo off
set TASK_NAME=HourlyQuickTest
set PYTHON_PATH=C:\Python312\python.exe
set SCRIPT_PATH=C:\Users\RhysL\Desktop\DE_Tools\Explorations\Other\Scheduled-Tasks\example_task.py
set START_TIME=08:00

schtasks /create ^
 /tn "%TASK_NAME%" ^
 /tr "\"%PYTHON_PATH%\" \"%SCRIPT_PATH%\"" ^
 /sc hourly ^
 /st %START_TIME% ^
 /f

echo Task "%TASK_NAME%" registered to run every hour starting at %START_TIME%.
pause
