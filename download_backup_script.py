import shutil

import requests

url = 'https://arxiv.org/pdf/1409.1556.pdf'
r = requests.get(
    url=url,
    verify=False,
    stream=True
)
r.raw.decode_content = True
with open("1409.1556.pdf", 'wb') as f:
    shutil.copyfileobj(r.raw, f)
