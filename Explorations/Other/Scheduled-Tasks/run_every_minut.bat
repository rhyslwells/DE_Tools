@echo off
:loop
C:\Python312\python.exe "C:\Users\RhysL\Desktop\DE_Tools\Explorations\Other\Scheduled-Tasks\example_task.py"
timeout /t 60
goto loop
