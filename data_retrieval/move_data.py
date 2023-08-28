import glob
import os

for sign_path in glob.glob("data/**"):
    for era_path in glob.glob(sign_path + "/**"):
        era = era_path.split('\\')[2]
        if era != 'Neo-Assyrian' and era != 'Neo-Babylonian' and era != "Ur III":
            for file_path in glob.glob(era_path + "/**"):
                file = file_path.split('\\')[3]
                print(file_path)
                os.rename(f'{file_path}',f'{sign_path + "/" + "Neo-Babylonian" + "/"+ file}')
            os.rmdir(era_path)