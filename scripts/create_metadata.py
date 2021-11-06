from brownie import network
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests
import json
import os

uploaded_imgs = {}
with open('./metadata/img-uris.json', 'r') as fp:
    uploaded_imgs = json.load(fp)

PINATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"

headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}

meta_uploads = {}

def make_dir(dir_path):
    Path(dir_path).mkdir(parents=True, exist_ok=True)

def main():
    for team_name, team_data in uploaded_imgs.items():
        for player_name, meta_up_data in team_data.items():
            dir_name = f"./metadata/{network.show_active()}/"
            make_dir(dir_name)
            metadata_file_name = (
                f"{dir_name}{team_name.replace(' ','_')}-{player_name.replace('.gif','')}.json"
            )
            collectible_metadata = metadata_template
            if Path(metadata_file_name).exists():
                print(f"{metadata_file_name} already exists! Delete it to overwrite")
            else:
                print(f"Creating Metadata file: {metadata_file_name}")
                collectible_metadata["name"] = player_name.replace('_',"").replace('.gif',"")
                collectible_metadata["description"] = f"{team_name}!"
                collectible_metadata["attributes"][0]["value"] = team_name
                image_uri = f"https://ipfs.io/ipfs/{meta_up_data['IpfsHash']}?filename={player_name}"
                collectible_metadata["image"] = image_uri
                with open(metadata_file_name, "w") as file:
                    json.dump(collectible_metadata, file)
                if os.getenv("UPLOAD_IPFS") == "true":
                    upload_to_ipfs(metadata_file_name)
    
    with open('./metadata/meta-uris.json', "w") as file:
        json.dump(meta_uploads, file)


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        binary = fp.read()
        filename = str(filepath).split('/')[-1]
        response = requests.post(
                PINATA_BASE_URL + endpoint,
                files={"file": (filename, binary)},
                headers=headers,
            )
        meta_uploads[filename] = response.json()

