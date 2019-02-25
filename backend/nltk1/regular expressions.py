__author__ = 'Harsh'
import re
ex="Delhi/Kolkata/Mumbai"
print(re.findall("(.*)/",ex))
print(re.findall("/(.*)/",ex))