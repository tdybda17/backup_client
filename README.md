<h1>Daily Database Backup</h1>
<ol>
    <li>
        Change url and paths in **download_backup_script.py** to the correct values (use absolute paths)
    </li>
    <li>
        Change _PATH_TO_PYTHON_EXE_ in **create_task.bat** to the absolute path to python.exe (can be found by typing _where python_ in the terminal)
    </li>
    <li>
        Change _PATH_TO_PYTHON_SCRIPT_ in **create_task.bat** to the absolute path to **download_backup_script.py**
    </li>
    <li>
        Open the task scheduler by entering _taskschd.msc_ into the terminal
    </li>
    <li>
        Find the newly created task **DailyDatabaseBackupTask** under **Active Tasks** and double-press it
    </li>
    <li>
        Press **Properties**. Change values to match your preferences. Most importantly, choose _Run whether user is logged on or not_ under **General** and check _Run task as soon as possible after a scheduled start is missed_ under **Settings**
    </li>
</ol>