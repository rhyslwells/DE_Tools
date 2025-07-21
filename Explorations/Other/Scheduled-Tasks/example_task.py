# C:\Users\RhysL\Desktop\DE_Tools\Explorations\Other\Scheduled-Tasks\example_task.py
#This appends the current timestamp to a `task_log.txt` file in the same directory

from datetime import datetime
import os

log_path = os.path.join(os.path.dirname(__file__), "task_log.txt")

with open(log_path, "a") as f:
    f.write(f"Task ran at: {datetime.now()}\n")
