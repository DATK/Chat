@echo off
Title Server running
start /B python Server.py
start /B python backup.py
:or start /B
:/MIN to no window