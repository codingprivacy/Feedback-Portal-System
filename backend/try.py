__author__ = 'Harsh Patel'
import json
import random

with open("form1.json") as file:
    data=json.load(file)

    print(len(data["p1"]))
    print(data["p1"][str( random.randint( 1,len(data["p1"]) ) )])

    print(data['p1'])
    if "p1" in data.keys():
        print('pass')