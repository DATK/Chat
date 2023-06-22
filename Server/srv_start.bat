@echo off
Title Server running
start /B python Server.py
start /B python backup.py
:start "" python cmd.py
start "" ngrok.exe http 5000
:or start /B
:/MIN to no window