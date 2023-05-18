@echo off
Title Server running
start /B python Server.py
start /B python backup.py
start /B python cmd.py
:or start /B
:/MIN to no window