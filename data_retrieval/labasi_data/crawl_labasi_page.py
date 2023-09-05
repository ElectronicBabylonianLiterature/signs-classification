from pathlib import Path

import requests

from utils import create_directory


def get_abz(url):
    try:
        abz_number = requests.get(url=url).json()["abz_number"]
    except ConnectionError as e:
        print(e)
        get_abz(url)
    return f"ABZ{abz_number}"


def get_signs(url, output):
    LABASI_ABZ_TO_EBL_ABZ = {
        "ABZ003": "ABZ3",
        "ABZ008": "ABZ8",
        "ABZ063 d": "ABZ63",
        "ABZ74, 100": "ABZ74",
        "ABZ74(47)": "ABZ74",
        "ABZ074(48)": "ABZ74",
        "ABZ104,6": "ABZ104_6",
        "ABZ122 b": "ABZ122b",
        "ABZ142 a": "ABZ142a",
        "ABZ152^8": "ABZ152_8",
        "ABZ295 m": "ABZ295m",
        "ABZ314 (167)": "ABZ314",
        "ABZ314 (168)": "ABZ314",
        "ABZ331 e": "ABZ331e+152i",
        "ABZ376*": "ABZ376",
        "ABZ459 a": "ABZ459a",
        "ABZ598 a": "ABZ598a",
    }
    signs_filter = {'ABZ597':'GAR', 'ABZ461':'KI', 'ABZ231':'NI', 'ABZ73':'TI', 'ABZ318':'U₂', 
                    'ABZ533':'MEŠ', 'ABZ15':'KA', 'ABZ139':'TA', 'ABZ354':'ŠU', 'ABZ308':'E', 'ABZ68':'RU'}
    print(url)
    resp = requests.get(url=url)
    data = resp.json()
    for result in data["results"]:
        img_url = result["image"]
        if img_url is not None:
            sign_name = get_abz(result["sign"])
            if sign_name in LABASI_ABZ_TO_EBL_ABZ:
                sign_name = LABASI_ABZ_TO_EBL_ABZ[sign_name]
            if sign_name in signs_filter:
                abz_sign_directory = output / signs_filter[sign_name]
                if not abz_sign_directory.exists():
                    create_directory(abz_sign_directory)
                resp = requests.get(url=img_url)
                name = f"{signs_filter[sign_name]}_{result['identifier']}.{img_url.split('.')[-1]}"
                with open(output / signs_filter[sign_name] / name, "wb") as f:
                    f.write(resp.content)
    if data["next"] is not None:
        get_signs(data["next"], output)


def map_to_ABZ(data):
    # iterate through directory
    LABASI_ABZ_TO_EBL_ABZ = {
        "ABZ003": "ABZ3",
        "ABZ008": "ABZ8",
        "ABZ063 d": "ABZ63",
        "ABZ74, 100": "ABZ74",
        "ABZ74(47)": "ABZ74",
        "ABZ074(48)": "ABZ74",
        "ABZ104,6": "ABZ104_6",
        "ABZ122 b": "ABZ122b",
        "ABZ142 a": "ABZ142a",
        "ABZ152^8": "ABZ152_8",
        "ABZ295 m": "ABZ295m",
        "ABZ314 (167)": "ABZ314",
        "ABZ314 (168)": "ABZ314",
        "ABZ331 e": "ABZ331e+152i",
        "ABZ376*": "ABZ376",
        "ABZ459 a": "ABZ459a",
        "ABZ598 a": "ABZ598a",
    }
    for elem in data.iterdir():
        # rename elem if elem is in mapping
        if elem.name in LABASI_ABZ_TO_EBL_ABZ:
            rename = LABASI_ABZ_TO_EBL_ABZ[elem.name]
            if (data / rename).exists():
                # copy all data
                elem.rename(elem.parent / LABASI_ABZ_TO_EBL_ABZ[elem.name])


if __name__ == "__main__":
    url = "http://labasi.acdh.oeaw.ac.at/data/api/glyphs/?limit=100&offset=3600"
    output = Path("./data")
    get_signs(url, output)
