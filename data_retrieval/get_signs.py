from pymongo import MongoClient
import sys
import os
from PIL import Image
import io
import base64
import tqdm
print("Enter connection string", sys.argv)

client  = MongoClient(sys.argv[1])
database = client["ebl"]
annotations = database["annotations"]
fragments = database["fragments"]
cropped_images = database["cropped_sign_images"]
sign_filter = ["GAR","KI", "NI", "U₂", "MEŠ", "KA", "TI", "TA", "ŠU", "E", "RU"]
counter = 0
for sign in tqdm.tqdm(sign_filter):
    image_id_era = {}
    if not os.path.isdir('data'):
            os.mkdir('data')
    pipeline = [
        {"$match" : {"annotations.data.signName": sign}},
        {"$unwind" : "$annotations"},
        {"$match": {"annotations.data.signName": sign}},
        {"$project": {"annotations.data.signName": 1, "annotations.croppedSign": 1, "fragmentNumber": 1}}
    ]
    cursor = annotations.aggregate(pipeline)
    for doc in tqdm.tqdm(cursor):
        image_id = doc['annotations']['croppedSign']['imageId']
        fragment_id = doc['fragmentNumber']
        fragment_cursor = fragments.find({"_id": fragment_id}, {"script.period":1})
        for fragment_doc in fragment_cursor:
            image_id_era[image_id] = fragment_doc['script']['period']
    for image in tqdm.tqdm(image_id_era):
        if image_id_era[image] == 'Neo-Babylonian' or image_id_era[image] == 'Neo-Assyrian':
            if not os.path.isdir(f'data/{sign}_{image_id_era[image]}'):
                os.mkdir(f'data/{sign}_{image_id_era[image]}')
        image_cursor = cropped_images.find({"_id": image})
        for doc in image_cursor:
            image_string = doc['image']
            img = Image.open(io.BytesIO(base64.decodebytes(bytes(image_string, "utf-8"))))
            if image_id_era[image] != 'Neo-Assyrian' and image_id_era[image] != 'Neo-Babylonian' and image_id_era[image] != "Ur III":
                if not os.path.isdir(f'data/{sign}_Neo-Babylonian'):
                    os.mkdir(f'data/{sign}_Neo-Babylonian')
                img.save(f'data/{sign}_Neo-Babylonian/{counter}.png')
            elif image_id_era[image] == 'Ur III':
                pass
            else:
                img.save(f'data/{sign}_{image_id_era[image]}/{counter}.png')    
        counter += 1