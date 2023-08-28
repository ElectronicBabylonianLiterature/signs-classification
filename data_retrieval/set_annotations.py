import glob
import json
annotations = open("data/annotations.csv", "w", encoding='utf-8')
mapping = {}
counter = 0
for image_path in glob.glob("data/**/**/*.png"):
    sign, era = image_path.split('\\')[1:3]
    if sign + "_" +  era not in mapping:
        mapping[sign + "_" + era] = counter
        counter += 1
    annotations.write(f'{image_path[5:]}, {mapping[sign + "_" + era]}\n')
annotations.close()
mapping = {v: k for k, v in mapping.items()}
with open('data/mapping', 'w') as fp:
    json.dump(mapping, fp)
