from pymongo import MongoClient
from gridfs import GridFS
import sys
import os
from PIL import Image
import io
import random
import base64
import tqdm
import json
print("Enter connection string", sys.argv)

client  = MongoClient(sys.argv[1])
database = client["ebl"]
fragments = database["fragments"]
photos = GridFS(database, "photos")
fragment_cursor = fragments.find({"script.period":"Neo-Assyrian"})
fragments = []
counter = 0
for doc in fragment_cursor:
    fragments.append(doc['_id'] + '.jpg')
    counter += 1    
    if counter >= 500:
        break
counter = 0
random.shuffle(fragments)
grids = photos.find({"filename": {"$in": fragments}})#fragments_NA}})
for grid in grids:
    counter += 1
    if counter >= 200:
        break
    print(counter)
    file_bytes = grid.read()
    with open(f"Fragments/NA/{grid.filename}", "wb") as imgfile:
        imgfile.write(file_bytes)
    
