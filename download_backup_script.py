import datetime
import json
import os
import shutil
from datetime import date

import requests

number_of_days_to_backup = 10
url = 'http://127.0.0.1:8000/backup/'
credentials_path = 'credentials.json'

today_str = str(date.today())  # current date in format YYYY-MM-DD
backup_output_path = 'path/to/backups/' + today_str + '-backup.tar.gz'

with open(credentials_path) as json_file:
    config = json.load(json_file)
r = requests.get(
    url=url,
    verify=False,
    stream=True,
    headers={'USER': config.get('USERNAME'), 'PASS': config.get('PASSWORD')}
)
r.raw.decode_content = True
with open(backup_output_path, 'wb') as f:
    shutil.copyfileobj(r.raw, f)

dir_path = os.path.dirname(backup_output_path)
list_of_files = os.listdir(dir_path)

if len(list_of_files) > number_of_days_to_backup:
    # sort files by the first 10 chars in the filename (corresponds to the date)
    list_of_files.sort(key=lambda x: datetime.datetime.strptime(x[:10], '%Y-%m-%d'))
    oldest_file = os.path.join(dir_path, list_of_files[0])
    os.remove(oldest_file)
