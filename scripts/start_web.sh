#| /bin/bash

cd ../web
ls
source venv/bin/activate
pip3 install -r requirements.txt
python3 server.py &