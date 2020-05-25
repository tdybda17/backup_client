import json
import shutil

import requests

url = 'http://127.0.0.1:8000/backup/'
credentials_path = 'credentials.json'
backup_output_path = 'somefile.tar.gz'
date = '2020-04-04'

with open(credentials_path) as json_file:
    config = json.load(json_file)

r = requests.get(
    url=url,
    verify=False,
    stream=True,
    headers={'USER': config.get('USERNAME'), 'PASS': config.get('PASSWORD'), 'Date': date},
)
r.raw.decode_content = True
with open(backup_output_path, 'wb') as f:
    shutil.copyfileobj(r.raw, f)
