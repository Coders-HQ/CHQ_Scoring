"""
Save all gh archive to mongo
"""

import gzip
import jsonlines
import requests
import os
from pymongo import MongoClient

   
# Making Connection 
myclient = MongoClient("mongodb://localhost:27017/")  
   
# database  
db = myclient["gh-archive"] 
 
Collection = db["event"] 

with open('ras.txt', 'w+') as save:
  day = range(23)
  for hour in day:
    file = '2021-01-17-'+str(hour+1)+'.json.gz'
    url = 'https://data.gharchive.org/'+file
    r = requests.get(url, allow_redirects=True)
    open(file, 'wb').write(r.content)
    with gzip.open(file,'rb') as reader:
      reader = jsonlines.Reader(reader)
      for obj in reader:
        Collection.insert_one(obj) 
    os.remove(file) 


