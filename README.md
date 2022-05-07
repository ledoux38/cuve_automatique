# cuve_automatique
# Install requirements.txt
 pip install -r requirements.txt

# if problem witch raise SerialException(msg.errno, "could not open port {}: {}".format(self._port, msg))
sudo chmod 777 /dev/ttyACM0

Settings configuration
script path: .../.../.../cuve_automatique/interface/back/venv/bin/flask

parameters: run

variables: FLASK_APP=flaskr;FLASK_ENV=development;FLASK_DEBUG=True;PYTHONUNBUFFERED=1

Documentations
https://flask.palletsprojects.com/en/1.1.x/tutorial/

#COPY
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"^((d|a):(\d+):(o|i))$"

test_str = ("d:1:o\n"
	"a:13:i\n")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
