import os
from pathlib import Path
import requests
import json 


PINATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"

headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}

image_uris = {}

def main():
    p = Path(r'./ipl-gifs/').glob('**/*')
    filepaths = [str(x) for x in p if x.is_file()]
    print(filepaths)
    # Change this filepath
    for filepath in filepaths:
        filename = filepath.split("/")[-1:][0]
        filename.replace(' ','_')
        team_name = filepath.split("/")[-2:][0]
        team_name.replace(' ','_')
        if not image_uris.get(team_name,None): 
            image_uris[team_name] = {}    
        image_uris[team_name][filename] = ''
        with Path(filepath).open("rb") as fp:
            image_binary = fp.read()
            response = requests.post(
                PINATA_BASE_URL + endpoint,
                files={"file": (filename, image_binary)},
                headers=headers,
            )
            image_uris[team_name][filename] = response.json()
    print(image_uris)
    with open('./metadata/img-uris.json', 'w') as fp:
        json.dump(image_uris,fp)


if __name__ == "__main__":
    main()
