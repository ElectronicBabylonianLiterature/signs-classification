import glob
import json
import os
annotations = open("CDP_data/annotations.csv", "w", encoding='utf-8')
mapping = {}
counter = 0
for image_path in glob.glob("CDP_data/**/**/*.jpeg"):
    sign, era, file = image_path.split('\\')[1:4]
    if sign + "_" +  era not in mapping:
        mapping[sign + "_" + era] = counter
        counter += 1
    annotations.write(f'{sign}\{era}\{file}, {mapping[sign + "_" + era]}\n')
annotations.close()
mapping = {v: k for k, v in mapping.items()}
with open('CDP_data/mapping', 'w') as fp:
    json.dump(mapping, fp)
