import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('/home/sanjay/Tacts/dead link/output.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient("mongodb+srv://crud:san@cluster0.mgpjl.mongodb.net/crud?retryWrites=true&w=majority") 
db=mongo_client.restdb
db.stars.drop()
header= [ "referer","status","url"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.stars.insert(row)
