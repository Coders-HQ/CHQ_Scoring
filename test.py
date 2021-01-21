import gzip
import jsonlines
import requests
import os
from pymongo import MongoClient

   
# Making Connection 
myclient = MongoClient("mongodb://localhost:27017/")  
   
# database  
db = myclient["gh-archive"] 
   
# Created or Switched to collection  
# names: GeeksForGeeks 
Collection = db["event"] 
  
# # Loading or Opening the json file 
# with open('2020-01-17-0.json') as file: 
#     reader = jsonlines.Reader(file)
#     for obj in reader:
      
#       # Inserting the loaded data in the Collection 
#       # if JSON contains data more than one entry 
#       # insert_many is used else inser_one is used 
#       if isinstance(obj, list): 
#           Collection.insert_many(obj)   
#       else: 
#           Collection.insert_one(obj) 

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

# with open('ras.txt', 'w+') as save:
#   file = '2020-01-17-'+'1'+'.json.gz'
#   url = 'https://data.gharchive.org/'+file
#   r = requests.get(url, allow_redirects=True)
#   open(file, 'wb').write(r.content)
#   with gzip.open(file,'rb') as reader:
#     reader = jsonlines.Reader(reader)
#     for obj in reader:
#         # if obj['actor']['login']=='ralsuwaidi':
#         if obj['type']=='PushEvent':
#           save.write(obj['repo']['name']+'\n')
#   os.remove(file) 

