from re import I
from pymongo import MongoClient
import sys
import os
import pandas
import shutil
sign_filter = ["AN","DIŠ", "A", "MA", "BAD", "AŠ", "IGI", "UD", "NA", "ŠU₂", "MU", "NU","GIŠ","I"]

print("Enter connection string", sys.argv)

client  = MongoClient(sys.argv[1])
database = client["ebl"]
fragments = database["fragments"]

data = pandas.read_excel('csvs/corrected_instance.xlsx')
sign_museum = data[data['sign_new'].isin(sign_filter)][['sign_new', 'museum_number','filename']]
sign_museum_dict = sign_museum.to_dict('tight',index=False)['data']
for idx, line in enumerate(sign_museum_dict):
    cursor = fragments.find_one({"_id":line[1].replace("_",".")}, {"script.period" : 1})
    if not cursor:
        del line
    else:   
        if cursor['script']['period'] != "None":
            line[1] = cursor['script']['period']
        else:
            del line
print(sign_museum_dict)
if not os.path.isdir('CDP_data'):
    os.mkdir('CDP_data')
for sign, era, filename in sign_museum_dict:
    if era in ['Neo-Assyrian', 'Neo-Babylonian']:
        if not os.path.isdir('CDP_data/' + sign + "_" + era):
                os.mkdir('CDP_data/' + sign + "_" + era)
        shutil.copy2(f"static/img/instance/{filename}.jpg", f'CDP_data/{sign}_{era}/{filename}.jpg')
        