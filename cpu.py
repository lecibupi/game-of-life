#!/usr/bin/python
#coding: utf-8
result = {}
with open ("/proc/cpuinfo","r") as f:
     contens = f.readlines()
     for line in contens:
	 splitlines = line.split(":")
	 key = splitlines[0].strip()
	 if len(splitlines) < 2:
             value = ""
	 else:
	     value = splitlines[1].strip()
	 result[key] = value
print(result)
