import os

from tqdm import tqdm
from dict_reader import DictReader

_target_dir = './dicts/'
_origin_file = './dicts/cmu.txt'


# Main
def main():
    # First read the origin file
    origin_dict = DictReader(_origin_file).dict
    # Scan all files in the directory
    for file in tqdm(sorted(os.listdir(_target_dir))):
        if file.endswith('.txt') and file != 'cmu.txt':



# Import a dictionary txt file
def import_dict(file) -> dict:
    with open(file, 'r') as f:
        for line in tqdm(f):
            line = line.strip()
