<h1>Daily Database Backup</h1>
<ol>
    <li>
        Change url and paths in <b>download_backup_script.py</b> to the correct values (use absolute paths)
    </li>
    <li>
        Change <i>PATH_TO_PYTHON_EXE</i> in <b>create_task.bat</b> to the absolute path to python.exe (can be found by typing <i>where python</i> in the terminal)
    </li>
    <li>
        Change <i>PATH_TO_PYTHON_SCRIPT</i> in <b>create_task.bat</b> to the absolute path to <b>download_backup_script.py</b>
    </li>
    <li>
        Open the task scheduler by entering <i>taskschd.msc</i> into the terminal
    </li>
    <li>
        Find the newly created task <b>DailyDatabaseBackupTask</b> under <b>Active Tasks</b> and double-press it
    </li>
    <li>
        Press <b>Properties</b>. Change values to match your preferences. Most importantly, choose <i>Run whether user is logged on or not</i> under <b>General</b> and check <i>Run task as soon as possible after a scheduled start is missed</i> under <b>Settings</b>
    </li>
</ol>