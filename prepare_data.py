import os

from tqdm import tqdm
from dict_reader import DictReader

_target_dir = './dicts/'
_origin_file = './dicts/cmu.txt'


# Main
def main():
    # First read the origin file
    origin_dict = DictReader(_origin_file).dict
    origin_cur_len = len(origin_dict)
    origin_additions = 0
    # Scan all files in the directory
    for file in tqdm(sorted(os.listdir(_target_dir))):
        if file.endswith('.txt') and file != 'cmu.txt':
            # Read the file
            target = DictReader(os.path.join(_target_dir, file)).dict
            # Add the new words to the origin dictionary
            origin_dict.update(target)
            # Count the additions
            diff = len(origin_dict) - origin_cur_len
            if diff > 0:
                origin_additions += diff
                origin_cur_len = len(origin_dict)




# Import a dictionary txt file
def import_dict(file) -> dict:
    with open(file, 'r') as f:
        for line in tqdm(f):
            line = line.strip()
